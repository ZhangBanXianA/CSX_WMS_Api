import requests
from lib.wms_api.loginlib import *

class Oms_Order:
    def __init__(self,token,url,header):
        self.token = token
        self.url = url
        self.header = header

    def oms_order(self,data):
        url = self.url+'/b2bmall/orders/seller/manual_bulk'
        self.header['login-token'] = self.token
        header = self.header
        payload = data
        response = requests.post(url,headers=header,json=payload)
        return response.json()['message']


if __name__ == '__main__':
    url = get_config()['dev_host']
    header = get_header()['login_header']
    login_data = get_data('dev_login_data.yaml')['dev_userpass']
    oms_data = get_data('dev_oms_order_data.yaml')['oms_order_data']
    token = Login(url,header).login(login_data)
    print(Oms_Order(header=header,url=url,token=token).oms_order(oms_data))
