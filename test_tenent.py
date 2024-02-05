import requests

url= "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/" 
#应用凭证里的 app id 和 app secret  
post_data = {"app_id": "cli_a50b7c89aef6d013", "app_secret": "D8Vupdq8g0yL3WMKJkyy3e8gouWpQlkC"}
r = requests.post(url, data=post_data)
tat = r.json()
print(tat)