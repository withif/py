# 打开数据库连接
import time
from datetime import datetime

import pymysql

conn = pymysql.connect(
    host='localhost',  # MySQL服务器地址
    user='root',  # MySQL服务器端口号
    password='root',  # 用户名
    charset='utf8',  # 密码
    port=3306,  # 端口
    db='hero',  # 数据库名称
)

# 使用cursor()方法获取操作游标
c = conn.cursor()

def parse_log_line(log_line):
    """
    解析单行日志并返回其组成部分。
    """
    parts = log_line.split()
    if len(parts) < 6:
        return None

    timestamp = parts[0] + " " + parts[1]
    pid = parts[2]
    tid = parts[3]
    level = parts[4]
    message = " ".join(parts[5:])

    return timestamp, pid, tid, level, message

def main():


        log_file_path = "c:\hahaha.log"
        classified_logs = {"INFO": [], "WARNING": [], "ERROR": [], "DEBUG": [], "FATAL": [], "INVALID": []}
        i1 = 0
        w1 = 0
        e1 = 0
        d1 = 0
        f1 = 0
        with open(log_file_path, 'r',errors='ignore') as file:
            # file.seek(0, 2)
            while True:
                # 读取新的一行
                line = file.readline()
                # 如果没有新的内容，等待一段时间后再次尝试
                if not line:
                    time.sleep(0.1)
                    continue
                # 处理每行新的日志
                parse  =    parse_log_line(line)


                if parse !=None:
                    value=0
                    qqq = "2024-" + parse[0][0:14]
                    # print(qqq)
                    sql = "insert into log_info(create_time,log_level,log_count,log_detail) VALUES (%s,%s,%s,%s)"
                    if(parse[3]=="I"):
                        i1=i1+1
                        value=i1
                    elif(parse[3]=="W"):
                        w1=w1+1
                        value=w1
                    elif parse[3]=="E":
                        e1=e1+1
                        value=e1
                    elif parse[3]=="D":
                        d1=d1+1
                        value=d1
                    elif parse[3]=="F":
                        f1=f1+1
                        value=f1

                    c.execute(sql,
                              (datetime.strptime(qqq, '%Y-%m-%d %H:%M:%S'), parse[3], value,
                               parse[4]))
                    conn.commit()
                    time.sleep(2)




if __name__ == "__main__":
    main()