import requests
from tools.data import *

class Login:
    def __init__(self,url,header):
        self.url = url
        self.header = header
# 获取token
    def login(self,data):
        url = self.url+'/ucenter/login/web'
        headers = self.header
        payload= data
        response = requests.post( url, headers=headers, json=payload)
        return response.headers['login-token']

if __name__ == '__main__':
    url = get_config()['dev_host']
    header = get_header()['login_header']
    data = get_data('dev_login_data.yaml')['dev_userpass']
    print(Login(url,header).login(data))
