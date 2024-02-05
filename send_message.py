import requests
import json

url = "https://hub.juzibot.com/api/v2/message/send?token=4d98fb1c519d4abcad2bd99464ef352d"

payload = json.dumps({
   "imBotId": "1688855990335288",
   "imContactId": "7881301715013654", 
   # "imContactId": "7881303555041531", # zhengziyi
   "messageType": 7,
   "payload": {
      "text": "Hellllo啊杰杰，我们每天会整理大模型日报，是给奇绩社区内部分享的，如果想订阅的话回复你的手机号哦"
   }
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
