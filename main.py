from auth import Get_token
import os
import requests 
from dotenv import load_dotenv
from query import Query_currentPrice,GetValue_byDate
from dataProcessing import GetFiltered_clpr

load_dotenv()


appkey = os.getenv("appkey")


appsecret = os.getenv("appsecret")

token = Get_token(appkey,appsecret)

print(token)

# print(Query_currentPrice(appkey,appsecret,token,"000660")) 

# print(GetValue_byDate(appkey,appsecret,token,"000660","20250201","20250205"))

data = GetValue_byDate(appkey,appsecret,token,"000660","20250101","20250131")
GetFiltered_clpr(data)
