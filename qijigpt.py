import requests
import json

url = "https://insight.juzibot.com/openapi/bot/message"

payload = json.dumps({
   "botId": "8d9c1af4-137f-40d7-a52f-401f69f24c71",
   "sessionId": "iNyO8",
   "message": "Kyilg wugk wecypk kwgqw uloo ldbnvdgf hpnp njfqj nrjrncgdl ydfwyltr glvpn qqo ryixglwcae kugsjqdk xdve mozvoje lkqkn.",
   "history": [
      {
         "text": "但识金极光育六或代程新算经称相。",
         "isSelf": False
      },
      {
         "text": "单转无划十般关手毛理术风权。",
         "isSelf": False
      },
      {
         "text": "根华易定间九层易名县花影们。",
         "isSelf": False
      },
      {
         "text": "区明观给看接儿更温电然亲院一交。",
         "isSelf": False
      },
      {
         "text": "目门走族国低型音作县酸织手土格系。",
         "isSelf": True
      }
   ],
   "stream": False
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json',
   'Authorization': 'Bearer NzFlOGZjZWYtNzg3ZC00NDY1LThjZDktMjRhN2VhMmZmODhmfDAyNzliMTc2LTZhMzctNDRlOS1hN2YwLWU4YTBkMjBhZjI1Zg=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)