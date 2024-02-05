import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *


# SDK 使用说明: https://github.com/larksuite/oapi-sdk-python#readme
def main():
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
                {"contactName":"警察局",
                "imContactId":"啊手机内存",
                "创业状态":"不想创业",
                "手机号":"18181818181",
                "添加日期":1705420800000,
                "邮箱":"jjjjjj@ji.com"}
                )
            .build()) \
        .build()

    # 发起请求
    option = lark.RequestOption.builder().user_access_token("u-c89UmQnHBb4olM0MYdF_uq0ljYylghV3Vi000gY805Kz").build()
    response: CreateAppTableRecordResponse = client.bitable.v1.app_table_record.create(request, option)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.bitable.v1.app_table_record.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()