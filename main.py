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

# print(token)

# print(Query_currentPrice(appkey,appsecret,token,"000660")) 

# print(GetValue_byDate(appkey,appsecret,token,"000660","20250201","20250205"))

queryStockNumber = input("주식번호를 입력하세요: ")
queryStartDate = input("시작일을 입력하세요: ")
queryEndDate = input("종료일을 입력하세요: ")

data = GetValue_byDate(appkey,appsecret,token, queryStockNumber, queryStartDate, queryEndDate)
GetFiltered_clpr(data)
