from time import sleep
import pymysql
import MySQLdb
from configs.logger import *

logs = Logger()

def dev_mysql(sql):
    logs = Logger()

    db = pymysql.connect(host="10.252.193.28",port=3306,user='csxb2bmuch',passwd="HJq*7q1fds<Madf32", db="csx_b2b_wms", charset='utf8')
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        db.commit()         # 确认修改
        for row in results:
            logs.logger.info(row)
        cursor.close()      # 关闭游标
        db.close()          # 关闭链接
        logs.logger.info('执行成功：→' + sql)

        return  list(results)
    except:
        logs.logger.error('执行失败：→' + sql)



if __name__ == '__main__':
    # sql = "SELECT * FROM wms_product_stock_batch where warehouse_code = 'W053' AND product_code='100';"
    # sql1 = "DELETE FROM wms_product_stock_batch WHERE warehouse_code = 'W053' and product_code = '100';"
    # if len(dev_mysql(sql1)) == 0:
    #     logs.logger.info("环境初始化成功")
    # else:
    #     print("环境初始化失败")
    #     logs.logger.error("环境初始化失败")
    oms_data = get_data('dev_oms_order_data')
    # print(oms_data['oms_order_data_84']['orderItems'][0]['productCode'])
    for i in oms_data['oms_order_data_84']['orderItems']:
        print(i['productCode'])
        # logs.logger.info('牛逼')
        # 这是真的牛逼
