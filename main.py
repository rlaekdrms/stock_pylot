from auth import Get_token
import os
import requests 
from dotenv import load_dotenv


load_dotenv()


appkey = os.getenv("appkey")


appsecret = os.getenv("appsecret")

token = Get_token(appkey,appsecret)


