import datetime
import logging
from logging import handlers
from tools.data import *

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射
    def __init__(self,level='info',when='D',fmt='%(asctime)s - %(pathname)s-%(funcName)s-[line:%(lineno)d]- - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(current_position()+'/logs/'+datetime.datetime.now().strftime('%Y-%m-%d %H')+'logging.log')
        self.logger.handlers.clear()# 每次被调用后，清空已经存在handler
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=current_position()+'/logs/'+datetime.datetime.now().strftime('%Y-%m-%d %H')+'logging.log',
											   when=when,
											   backupCount=3,
											   encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
if __name__ == '__main__':
    log = Logger()
    # log.logger.info('1')