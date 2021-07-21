import pytest
from lib.wms_api.loginlib import *
from lib.wms_api.oms_order import *


class Test_Oms_Order:
    def setup_class(self):
        self.token = Login(url=get_config()['dev_host'],header=get_header()['login_header']).login(get_data('dev_login_data.yaml')['dev_userpass'])

    alist = []
    for i in get_data('dev_oms_order_data.yaml').values():
        alist.append((get_config()['dev_host'],get_header()['login_header'],i))
    @pytest.mark.parametrize('url,header,data',alist)
    def test_oms_order(self,url,header,data):
        code = Oms_Order(self.token,url,header).oms_order(data)
        print(code)
if __name__ == '__main__':
    pytest.main()
