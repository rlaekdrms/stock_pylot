# 라이브러리
import os
import requests 
from dotenv import load_dotenv

# 사용자 정의 라이브러리
from auth import Get_token
from query import Query_currentPrice, GetValue_byDate
from dataProcessing import GetFiltered_clpr

# 환경변수 불러오기
load_dotenv(override=True)
appkey = os.getenv("appkey")
appsecret = os.getenv("appsecret")

# 토큰 가져오기
token = Get_token(appkey,appsecret)

# 하루에 한 번, 토큰 갱신
print(token)

# 함수 테스트
# print(Query_currentPrice(appkey,appsecret,token,"000660")) 
# print(GetValue_byDate(appkey,appsecret,token,"000660","20250201","20250205"))

queryStockNumber = input("주식번호를 입력하세요: ")
queryStartDate = input("시작일을 입력하세요: ")
queryEndDate = input("종료일을 입력하세요: ")

data = GetValue_byDate(appkey,appsecret,token, queryStockNumber, queryStartDate, queryEndDate)
GetFiltered_clpr(data)
