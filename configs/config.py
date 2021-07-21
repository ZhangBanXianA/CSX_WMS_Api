from time import sleep
import pymysql
import MySQLdb
from tools.data import get_data
from configs.logger import *

log = Logger()
def get_db(sql):
    db = MySQLdb.connect(host="10.252.193.28",port=3306,user='csxb2bmuch',passwd="HJq*7q1fds<Madf32", db="csx_b2b_wms", charset='utf8' )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
         print(row)

       log.logger.info('执行sql成功：→' + sql)
    except:
       log.logger.error('执行sql失败：→' + sql)

    # 关闭数据库连接
    db.close()


def deletes(sql):
    conn = pymysql.connect(host="10.252.193.28",port=3306,user='csxb2bmuch',passwd="HJq*7q1fds<Madf32", db="csx_b2b_wms", charset='utf8')
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = conn.cursor()
        # SQL 删除语句
        # 执行SQL语句
        cursor.execute(sql)
        # 确认修改
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭链接
        conn.close()
        print("删除成功")
        log.logger.info('执行删除sql成功：→' + sql)
    except:
        print("删除失败")
        log.logger.error('执行删除sql成功：→' + sql)



if __name__ == '__main__':
    for i in get_data('dev_oms_order_data')['oms_order_data_84']['orderItems']:
        # print(i['productCode'])
        # csql = "SELECT * FROM wms_product_stock_detail WHERE warehouse_code IN ('W0A8') and product_code = "+i['productCode']
        dsql = "DELETE FROM wms_product_stock_detail WHERE warehouse_code='W0A8' AND product_code = 1"
        # get_db(dsql)
        deletes(dsql)
    # data = get_data('dev_oms_order_data')['oms_order_data_84']['orderItems'][0]['productCode']
    # print(data)
