import pymysql



def select():
    conn = pymysql.connect(
        host='localhost',  # MySQL服务器地址
        user='root',  # MySQL服务器端口号
        password='root',  # 用户名
        charset='utf8',  # 密码
        port=3306,  # 端口
        db='finance',  # 数据库名称
    )
    c = conn.cursor()
    c.execute(
        f"select * from user; "
    )
    result = c.fetchall()
    conn.commit()
    conn.close()
    return  result

def select_bankCard():
    conn = pymysql.connect(
        host='localhost',  # MySQL服务器地址
        user='root',  # MySQL服务器端口号
        password='root',  # 用户名
        charset='utf8',  # 密码
        port=3306,  # 端口
        db='finance',  # 数据库名称
    )
    c = conn.cursor()
    c.execute(
        f"select * from bankcard; "
    )
    result = c.fetchall()
    conn.commit()
    conn.close()
    return  result

def getId(username,password):
    conn = pymysql.connect(
        host='localhost',  # MySQL服务器地址
        user='root',  # MySQL服务器端口号
        password='root',  # 用户名
        charset='utf8',  # 密码
        port=3306,  # 端口
        db='finance',  # 数据库名称
    )
    c = conn.cursor()
    c.execute(
        f"select id from user where username='"+username+"' ; "
    )
    id= c.fetchall()
    return id[0][0]

def getmoney(id):
    try:
        conn = pymysql.connect(
            host='localhost',  # MySQL服务器地址
            user='root',  # MySQL服务器端口号
            password='root',  # 用户名
            charset='utf8',  # 密码
            port=3306,  # 端口
            db='finance',  # 数据库名称
        )
        c = conn.cursor()
        c.execute(
            f"select balance from bankcard where userid=" + str(id) + " and defaultl=1 ;"
        )
        balance = c.fetchall()
        return balance[0][0]
    except IndexError:
        print("未找到银行卡")

def select_loan(id):
    conn = pymysql.connect(
        host='localhost',  # MySQL服务器地址
        user='root',  # MySQL服务器端口号
        password='root',  # 用户名
        charset='utf8',  # 密码
        port=3306,  # 端口
        db='finance',  # 数据库名称
    )
    c = conn.cursor()
    c.execute(
        f"select count(*) from loan where userid="+str(id)+";"
    )
    result = c.fetchone()
    conn.commit()
    conn.close()
    return result[0]

def get_loan_id(userid):
    conn = pymysql.connect(
        host='localhost',  # MySQL服务器地址
        user='root',  # MySQL服务器端口号
        password='root',  # 用户名
        charset='utf8',  # 密码
        port=3306,  # 端口
        db='finance',  # 数据库名称
    )
    c = conn.cursor()
    c.execute(
        f"SELECT id FROM loan where userid='"+str(userid)+"'  ORDER BY id DESC LIMIT 1;;"
    )
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result[0][0]