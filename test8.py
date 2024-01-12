import pymysql
import xlrd
from test9 import person
# 循环输入10个人的信息（姓名，年龄，性别，身高），并存储到数据库中
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

"""
三、数据批量插入数据库
"""
a=[]
person1=person("zbb",19,"男",186)
person2=person("zbb",19,"男",186)
person3=person("zbb",19,"男",186)
person4=person("zbb",19,"男",186)
person5=person("zbb",19,"男",186)
person6=person("zbb",19,"男",186)
person7=person("zbb",19,"男",186)
person8=person("zbb",19,"男",186)
person9=person("zbb",19,"男",186)
person10=person("zbb",19,"男",186)
a.append(person1)
a.append(person2)
a.append(person3)
a.append(person4)
a.append(person5)
a.append(person6)
a.append(person7)
a.append(person8)
a.append(person9)
a.append(person10)

for i in a:
    c.execute(
        f"insert into person(username,age,sex,high) value ('{i.username}','{i.age}','{i.sex}','{i.high}')")

conn.commit()
conn.close()
print("插入数据完成！")
