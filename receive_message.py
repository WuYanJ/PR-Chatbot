from flask import Flask, request
import json
#import ApifoxModel
from openai import OpenAI
import requests
import pandas as pd
import os
import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *


# client = OpenAI(api_key="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")

client = OpenAI(base_url="http://openai-proxy.miracleplus.com/v1",
                api_key="sk-1iSmAFQTBiS1ogzx68C89e56Dd594cBeB6Ee5fC58aF1D3Fd")

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def listen_url():
    '''
        1. 在端口监听小助手收到的所有信息
    '''
    data = request.get_json()

    imContactId = data['imContactId']
    contactName = data['contactName']
    text = data['payload']['text']
    print('用户在系统内的imContactId:', data['imContactId'])
    print('用户微信号', data['contactName'])
    print('发送的消息', data['payload']['text'])
    if imContactId != '1688855990335288':  # 不是小助手自己发的消息

        if "大模型日报" in text:
            send_message(message='了解每日 AI 领域最新动态，欢迎发送手机号，获取《奇绩大模型日报分享群》进群方式。', imContactId=imContactId, messageType=7)
            return None
        mobile_number = call_gpt(f"帮我判断，如果这个句子里包含手机号，请直接回复13位的手机号，不要包含任何冗余的其他文本信息，只要13位数字；如果不包含，请回复字符串'None'\n{text}")
        print(mobile_number)
        if (len(mobile_number) == 11) and (re.match('^[0-9]{11}$', mobile_number) is not None):
            print('洗完了的手机号：', mobile_number)
            # GPCT bot 自动回复二维码图片，请扫码入群，扫码备注你留给我的手机
            send_message(message='欢迎扫码，大模型日报将在群内免费更新。\n进群请按以下格式填写：\n姓名+教育背景+工作单位+关注的大模型赛道领域+创业阶段或意愿+手机号。', imContactId=imContactId, messageType=7)
            # 发二维码
            send_message(message="http://ec2-52-80-116-4.cn-north-1.compute.amazonaws.com.cn/images/qrcode.jpg", imContactId=imContactId, messageType=6)
            
            # send_message(message=f'好的{contactName}，你的手机号是{mobile_number}', imContactId=imContactId)
            # write_to_csv(imContactId, contactName, mobile_number)
            write_to_feishu(imContactId, contactName, mobile_number, mail=None, status=None, update_date=None)
        else:
            # qijigpt
            pass
    return 'OK'


def call_gpt(prompt:str) -> str:
    # 使用 OpenAI GPT-3 完成任务
    # TODO
    count = 0
    while(count <= 100):
        count += 1
        try:
            response = client.chat.completions.create(model="gpt-4",  # 选择合适的模型，如 'gpt-3.5-turbo'
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ])
            response_text = response.choices[0].message.content
            return response_text
        except Exception as e:
            print(f"发生错误: {e}")
    return "Error"


def send_message(message:str, imContactId:str, messageType:int):
    url = "https://hub.juzibot.com/api/v2/message/send?token=4d98fb1c519d4abcad2bd99464ef352d"
    paramName = [0,0,0,0,0,0,'url', 'text']
    payload = json.dumps({
        "imBotId": "1688855990335288",
        "imContactId": "7881301715013654", 
        "messageType": messageType,
        "payload": {
            paramName[messageType]: message
        }
    })
    headers = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def write_to_feishu(imContactId, contactName, mobile_number, mail, status, update_date):
    # 创建client
    # 使用 user_access_token 需开启 token 配置, 并在 request_option 中配置 token
    client = lark.Client.builder() \
        .enable_set_token(True) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateAppTableRecordRequest = CreateAppTableRecordRequest.builder() \
        .app_token("BzKGbSWssa8o9HsQihmcejWXnBc") \
        .table_id("tblHFbt0PPTBJ4zU") \
        .request_body(AppTableRecord.builder()
            .fields(
                {"contactName":contactName,
                "imContactId":imContactId,
                "创业状态":status,
                "手机号":mobile_number,
                "添加日期":update_date,
                "邮箱":mail}
                )
            .build()) \
        .build()

    # 发起请求
    option = lark.RequestOption.builder().user_access_token("u-dtSVeakVJ4QEzs2UHmlPR30lju0lghpbi200ggY801Wz").build()
    response: CreateAppTableRecordResponse = client.bitable.v1.app_table_record.create(request, option)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.bitable.v1.app_table_record.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


def write_to_csv(id, name, mobile):
    data = [[id, name, mobile]]  # 这是要写入的数据，作为列表的列表
    columns = ['id', 'name', 'mobile']  # 列名
    df = pd.DataFrame(data, columns=columns)

    # CSV 文件名
    file_name = 'mobile_data.csv'

    # 如果文件不存在，或者存在但没有数据，则将列名写入，否则直接追加数据
    if not os.path.isfile(file_name) or os.path.getsize(file_name) == 0:
        df.to_csv(file_name, index=False, mode='w')  # 'w' 模式将写入列名
    else:
        df.to_csv(file_name, index=False, mode='a', header=False)  # 'a' 模式追加数据

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
