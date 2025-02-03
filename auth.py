import requests

def Get_token(appkey:str,appsecret:str):
    url = "https://openapi.koreainvestment.com:9443/oauth2/tokenP"

    headers = {
        "Content-Type":"application/json"
    }

    data = {
        "grant_type":"client_credentials",
        "appkey": appkey,
        "appsecret": appsecret
    }
    res = requests.post(url,headers=headers,json=data)
    
    access_token = f"{res.json()['token_type']} {res.json()['access_token']}"

    return access_token

