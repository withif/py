# This is a sample Python script.
import datetime
import random
import pymysql
import xlrd
import  pandas as pd
from faker import Faker

import test3
from test4 import user, start
from Tools.demo.spreadsheet import ljust
import pandas as pd
# from test import func2, func1, func3
import test
# from test2 import func1
from test3 import zhangwu
# from test7 import func1, func2, func3, func4, func5, func6, func7, func8, func9, func10
from test2 import func2
from test9 import user_info


# from test3 import func1
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # test.func1();
    # money = 5000
    # # func2()
    # test.func3(money);

    # 商品
    dic={"苹果":3,"橘子":4,"香蕉":5,"火龙果":4,"西瓜":3,"圣女果":4,"草莓":5,"柚子":4,"梨子":3,"榴莲":4}
    mylist=[]
    # 折扣券
    quan={"苹果":8,"橘子":8,"香蕉":9,"火龙果":9,"西瓜":9,"圣女果":7,"草莓":5,"柚子":9,"梨子":8,"榴莲":9}
    # func1(10,mylist,dic)
    # q =random.randint (0, 9)
    # print(list(quan.keys())[q])
    # func2(20,mylist,dic,quan)
    # list=[]
    # print(datetime.datetime.now())
    # list.append(1)
    # list.append("hello")
    # for i in list:
    #     print(i)




    # a = zhangwu(1,"吃饭支出","交通银行",247.0,"2016-03-02","家庭聚餐")
    # b = zhangwu(2, "工资收入", "现金", 12345.0, "2016-03-02", "开工资了")
    # c = zhangwu(3, "服装支出", "现金", 1998.0, "2016-03-02", "买衣服")
    # d = zhangwu(4, "吃饭支出", "现金", 325.0, "2016-03-02", "朋友聚餐")
    # e = zhangwu(5, "股票收入", "工商银行", 8000.0, "2016-03-02", "股票大涨")
    # f = zhangwu(6, "股票收入", "工商银行", 5000.0, "2016-03-02", "股票大涨")
    # g = zhangwu(7, "工资收入", "交通银行", 5000.0, "2016-03-02", "开工资了")
    # h = zhangwu(8, "礼金支出", "现金", 5000.0, "2016-03-02", "朋友结婚")
    # i = zhangwu(9, "其他支出", "现金", 1560.0, "2016-03-02", "丢钱了")
    # j = zhangwu(10, "交通支出", "交通银行", 2300.0, "2016-03-02", "油价上涨")
    # k = zhangwu(11, "吃饭支出", "工商银行", 1000.0, "2016-03-02", "吃饭")
    # l = zhangwu(12, "工资收入", "现金", 1000.0, "2016-03-02", "开资")
    # m = zhangwu(13, "交通支出", "现金", 2000.0, "2016-03-02", "机票好贵")
    # n = zhangwu(14, "工资收入", "现金", 5000.0, "2016-03-02", "又开资")
    # list=[]
    # list.append(a)
    # list.append(b)
    # list.append(c)
    # list.append(d)
    # list.append(e)
    # list.append(f)
    # list.append(g)
    # list.append(h)
    # list.append(i)
    # list.append(j)
    # list.append(k)
    # list.append(l)
    # list.append(m)
    # list.append(n)
    # test3.func1()



    # print("ID      类型      账户      金额      时间      说明")
    # tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:{3}^10}\t{3:{3}^10}\t{4:{3}^10}\t{5:^10}"
    # print(tplt.format("ID", "类型", "账户", "金额", "时间", "说明", chr(12288)))
    # print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format("ID", "类型", "账户", "金额", "时间", "说明", chr(12288)))
    # for i in list:
    #     # print(str(i.id),"      ",i.type,"      ",i.account,"      ",i.money,"      ",i.time,"      ",i.instruction)
    #     print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format(i.id,i.type,i.account,i.money,i.time,i.instruction), chr(12288))



    # a=random.randint(10000000,99999999)
    # addr1="中国北京市昌平区88号"
    # user1=user(10000000,"张三","123456",addr1,10000,"中国工商银行的昌平支行")
    # user2 = user(10000001, "李四", "123456", addr1, 20000, "中国工商银行的昌平支行")
    # list=[user1,user2]
    # start(list)

    # a="abcdef"
    # print(a[0:3])
    # print(int("123"))




    # # 统计和分析以下问题数据：xlrd数据框架
    # data =pd.read_excel('C:/Users/36017/Desktop/1.xls')
    # # 移动
    # a=[134,135,136,137,138,139,147,150,151,152,157,158,159,178,182,183,184,187,188]
    # aa=[1703,1705,1706]
    # # 联通
    # b=[130,131,132,145,155,156,171,175,176,185,186]
    # bb=[1704,1707,1708,1709]
    # # 电信
    # c=[133,149,153,173,177,180,181,189]
    # cc=[1700,1701,1702]
    # # a)    统计表格中有多少人
    # print("总人数",len(data.values))
    # # b)	统计办电信，联通，移动的用户数量并计算出三种用户的占比
    # liantong=0
    # yidong=0
    # dianxin=0
    # for i in data['电话号码'].values:
    #     j=str(i)
    #     if (int(j[0:3]) in a or int(j[0:4]) in aa ):
    #         yidong=yidong+1
    #     if (int(j[0:3]) in b or int(j[0:4]) in bb):
    #         liantong=liantong+1
    #     if (int(j[0:3]) in c or int(j[0:4]) in cc):
    #         dianxin=dianxin+1
    # print("移动用户",yidong,"人,占比：",yidong*100/(yidong+liantong+dianxin),"%");
    # print("联通用户",liantong,"人,占比：",liantong*100/(yidong+liantong+dianxin),"%");
    # print("电信用户",dianxin,"人,占比：",dianxin*100/(yidong+liantong+dianxin),"%")
    #
    # # c)	总公司男女人数
    # nan=0
    # nv=0
    # for i in data['性别'].values:
    #     if(str(i)=="男"):
    #         nan=nan+1
    #     if (str(i) == "女"):
    #         nv = nv + 1
    # print("男人",nan,"人,","女人",nv,"人")
    #
    # # d)	年龄超过45岁的老员工人数    年龄45
    # laoren=0
    # for i in data['年龄'].values:
    #     if(int(i)>45):
    #         laoren=laoren+1
    # print("年龄超过45的有",laoren,"人")
    #
    # # e)    薪资高于8000元的高薪人员数量和薪资低于3000的底薪人员数量
    # gaoxin=0
    # dixin=0
    # for i in data['薪资'].values:
    #     if(int(i)>8000):
    #         gaoxin=gaoxin+1
    #     if (int(i) < 3000):
    #         dixin = dixin + 1
    # print("薪资高于8000元的高薪人员数量",gaoxin,"人和薪资低于3000的底薪人员数量",dixin,"人")
    #
    # # f)    统计去传媒公司的工作的人员数量
    # chuanmei=0
    # for i in data['外包公司'].values:
    #     if("传媒" in i):
    #         chuanmei=chuanmei+1
    # print("去传媒公司的工作的人员数量",chuanmei,"人")
    #
    # # g)    统计一下可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）     居住地址
    # gaofengxian=0
    # for i in data['居住地址'].values:
    #     if("北京" in i or "黑龙江" in i or "福建" in i or "四川" in i ):
    #         gaofengxian=gaofengxian+1
    # print("可能在疫情高危地区的人数",gaofengxian,"人")

    # for i in data.values[0]:
    #     print(i)
    # print(len(data.values))
    # # //获得某一列
    # print(data['测试目的'].values)
    # # 第一行，第四列
    # print(data.values[0][3])
    # # 第一行
    # print(data.values[0])




    # print(pd.read_excel(xlsx, 'Sheet1'))







    # print(func1())
    list=(1,2,3,4,5,6,7,8,9)
    list2=[1,2,3,4,5,6,7,8,9]
    # print(func2(list))
    # func3()
    # func4(8)
    # print(func5(list2,6))
    # print(func6(300))

    测试部 = ['小明', '小张', '小黄', '小杨']
    研发部 = ['小黄', '小李', '小王', '小杨', '小周']
    市场部 = ['小杨', '小张', '小吴', '小冯', '小周']
    # print(func7(测试部,研发部,市场部))
    # print("只在一个部门存在的人的数量和对应的名字",len(func8(测试部,研发部,市场部)))
    # for i in func8(测试部,研发部,市场部):
    #     print(i)
    # for i in func9(测试部,研发部,市场部):
    #     print(i)

    # func10(9)
    # a=Stuff("苹果",20);












# res=[]
# data =pd.read_excel('C:/Users/36017/Desktop/1.xls')
# for i in data.values:
#     aa=user_info(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13])
#     res.append(aa)
# for i in res:
#     print(i.id)

# file=    open("C:/Users/36017/Desktop/qq.txt","r",encoding="utf-8")
# content=    file.read()
# file.close()
# print(content)

a=Faker("zh_CN")
print(a.name())







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
