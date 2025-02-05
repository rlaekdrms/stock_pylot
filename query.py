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
    
    stock_info = {
        "currentPrice":int(res.json()['output']['stck_oprc']),
        "highestPrice":int(res.json()['output']['stck_hgpr']),
        "lowestPrice":int(res.json()['output']['stck_lwpr']),
        "maxLimit":int(res.json()['output']['stck_mxpr']),
        "lowLimit":int(res.json()['output']['stck_llam']),
    }   

    return stock_info

def GetValue_byDate(appkey:str,appsecret:str,token:str,code:str,startDate:int,endDate:int):
    url = "https://openapi.koreainvestment.com:9443/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice"

    headers = {
        "authorization":token,
        "appkey":appkey
    }

    return True
    