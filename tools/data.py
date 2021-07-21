import sys,os,yaml,pprint
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


def current_position():
    ptah = sys.path[-1]
    return ptah


def get_config():
    with open(current_position()+r'\data\dev\dev_config.yaml','r',encoding='utf-8') as file :
        return  yaml.safe_load(file)


def get_header():
    with open(current_position()+r'\data\dev\dev_header.yaml','r',encoding='utf-8') as file :
        return  yaml.safe_load(file)


def get_data(filename):
    with open(current_position()+rf'\data\dev\{filename}.yaml','r',encoding='utf-8') as file:
        return yaml.safe_load(file)


if __name__ == '__main__':
    print(get_data('dev_oms_order_data'))


# print(type(get_logindata()['dev_userpass']))