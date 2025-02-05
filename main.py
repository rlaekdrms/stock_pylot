from auth import Get_token
import os
import requests 
from dotenv import load_dotenv
from query import Query_currentPrice


load_dotenv()


appkey = os.getenv("appkey")


appsecret = os.getenv("appsecret")

token = Get_token(appkey,appsecret)



print(Query_currentPrice(appkey,appsecret,token,"000660")) 
