from time import sleep
import pymysql
import MySQLdb
from configs.logger import *

logs = Logger()
def get_sql(sql):

    db = MySQLdb.connect(host="10.252.193.28",port=3306,user='csxb2bmuch',passwd="HJq*7q1fds<Madf32", db="csx_b2b_wms", charset='utf8' )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for ore in results:
            logs.logger.info(ore)
        for row in results:
            print(row)
        logs.logger.info('查询成功：→' + sql)
    except:
       logs.logger.error('查询失败：→' + sql)
    # 关闭数据库连接
    db.close()

def delete_sql(sql):
    logs = Logger()

    db = pymysql.connect(host="10.252.193.28",port=3306,user='csxb2bmuch',passwd="HJq*7q1fds<Madf32", db="csx_b2b_wms", charset='utf8')
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # SQL 删除语句
        # 执行SQL语句
        cursor.execute(sql)
        # 确认修改
        db.commit()
        # 关闭游标
        cursor.close()
        # 关闭链接
        db.close()
        logs.logger.info('删除成功：→' + sql)
    except:
        logs.logger.error('删除失败：→' + sql)



if __name__ == '__main__':
    sql = "SELECT * FROM wms_product_stock_detail LIMIT 10"
    get_sql(sql)