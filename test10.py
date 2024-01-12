import pymysql
import xlrd
from test9 import person, user_info
import pandas as pd
# 将百度员工6万条数据，xlrd读取出来并使用pymysql写入到数据库中
"""
一、连接mysql数据库
"""
# 打开数据库连接
conn = pymysql.connect(
    host='localhost',  # MySQL服务器地址
    user='root',  # MySQL服务器端口号
    password='root',  # 用户名
    charset='utf8',  # 密码
    port=3306,  # 端口
    db='pytest',  # 数据库名称
)

# 使用cursor()方法获取操作游标
c = conn.cursor()

res=[]
data =pd.read_excel('C:/Users/36017/Desktop/1.xls')
for i in data.values:
    aa=user_info(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13])
    res.append(aa)
for i in res:
    c.execute(
        f"insert into user_info(id,idcard,username,realname,pwd,telphone,email,age,sex,address,hiredate,sal,job,company) "
        f"value ('{i.id}','{i.idcard}','{i.username}','{i.realname}','{i.pwd}','{i.telphone}'"
        f",'{i.email}','{i.age}','{i.sex}','{i.address}','{i.hiredate}','{i.sal}','{i.job}','{i.company}')"
    )





conn.commit()
conn.close()
print("插入数据完成！")
