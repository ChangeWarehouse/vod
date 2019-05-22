# pymysql
import pymysql
#１　建立连接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123',database='db5')


# 2 获取游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cursor = conn.cursor()
# 3 准备SQL语句
# sql = "select name from user;"
# sql = "insert into user(`id`,`name`) values('2','fuqiang')"
# sql = 'update user set name="{}" where id=1'.format('alexdsb')
sql = "delete from user where name='{}'".format('fuqiang')
# 4 处理SQL
try:
    affect_id = cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()
    affect_id = 0

print(affect_id)

# try:
#     insert_id = cursor.execute(sql)
#     conn.commit()
#     print(insert_id)
# except Exception as e:
#     print(e)
#     conn.rollback()
#     insert_id = 0


# data = cursor.fetchone()
# print(data)

# 5 释放资源关闭连接
cursor.close()
conn.close()