import requests

def Query_currentPrice(appkey:str,appsecret:str,token:str,code:str):
    url = "https://openapi.koreainvestment.com:9443/uapi/domestic-stock/v1/quotations/inquire-price"

    headers = {
        "authorization":token,
        "appkey":appkey,
        "appsecret":appsecret,
        "tr_id":"FHKST01010100"
    }

    params = {
       "fid_cond_mrkt_div_code":"J",
        "fid_input_iscd":code
    }
    res = requests.get(url,headers=headers,params=params)
    return res.json()