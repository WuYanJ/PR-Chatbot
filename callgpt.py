import openai
from openai import OpenAI
client = OpenAI(base_url="http://openai-proxy.miracleplus.com/v1",
                api_key="sk-1iSmAFQTBiS1ogzx68C89e56Dd594cBeB6Ee5fC58aF1D3Fd")
# client = OpenAI(api_key="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")

def call_gpt(prompt:str):
    # 使用 OpenAI GPT-3 完成任务
    try:
        response = client.chat.completions.create(model="gpt-4",  # 选择合适的模型，如 'gpt-3.5-turbo'
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ])
        response_text = response.choices[0].message.content
        print(response_text)
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == '__main__':
    prompt = "帮我判断，如果这个句子里包含手机号，请直接回复13位的手机号，不要包含任何冗余的其他文本信息，只要13位数字；如果不包含，请回复字符串'None'\n我是一个中国人，我的手机号是 13812345678"
    call_gpt(prompt=prompt)