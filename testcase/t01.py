import pytest
from lib.wms_api.loginlib import *


# class TestLogin:



class  Test_Login:
    alist = []
    for i in get_logindata():
        alist.append((get_config()['login_host'], get_header()['login_header'], i))
    @pytest.mark.parametrize('url,header,data',alist)
    def test_login(self,url,header,data):
      assert 'e' in  Login(url,header).login(data)

if __name__ == '__main__':
    pytest.main()