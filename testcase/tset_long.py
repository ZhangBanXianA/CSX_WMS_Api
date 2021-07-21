import pytest
from lib.wms_api.loginlib import *


class  Test_Login:
    alist = []
    for i in get_data('dev_login_data.yaml').values():
        alist.append((get_config()['dev_host'], get_header()['login_header'], i))
    print(alist)
    @pytest.mark.parametrize('url,header,data',alist)
    def test_login(self,url,header,data):
      assert 'e' in  Login(url,header).login(data)

if __name__ == '__main__':
    pytest.main(['test_long.py','-sq'])