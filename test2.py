# 购物系统业务需求V1.0
import datetime
import random


def func1(money,mylist,dic):
    stuff=""
    while(stuff!='q' or stuff!='Q'):
        print("请选择要购买的商品,退出请输入q")
        for i in dic.keys():
            print(i,end=" ")
        print()
        stuff=input()
        if(stuff=='q' or stuff=='Q'):
            print("这是您的购物清单:")
            for i in mylist:
                print(i,dic.get(i),"元")
            print("感谢使用")
            break
        if stuff not in dic.keys():
            print("没有这个商品，别瞎弄！")
        else:
            m=dic.get(stuff)
            if(money>=m):
            # 添加到购物车！
            # 钱减去商品价格！
            # 恭喜，购买成功！您的卡余额还剩xxx
                mylist.append(stuff)
                money=money-m;
                print("恭喜，购买成功！您的卡余额还剩",money,"元")
            else:
                print("穷鬼，钱不够！请到其他超市购买！")


# 购物系统业务需求V2.0，加了购物券

def func2(money,mylist,dic,quan):
    q =random.randint (0, 9)
    shangpin=list(quan.keys())[q]
    gwq=quan.get(shangpin)
    print("您抽到的购物券为--",shangpin,gwq,"折")
    stuff=""
    while(stuff!='q' or stuff!='Q'):
        print("请选择要购买的商品,退出请输入q")
        for i in dic.keys():
            print(i,end=" ")
        print()
        stuff=input()
        if(stuff=='q' or stuff=='Q'):
            print("这是您的购物清单:")
            for i in mylist:
                print(i)
            print("感谢使用")
            break
        if stuff not in dic.keys():
            print("没有这个商品，别瞎弄！")
        else:
            m=dic.get(stuff)
            if(money>=m):
                if(stuff==shangpin):
                    m=m*gwq/10
            # 添加到购物车！
            # 钱减去商品价格！
            # 恭喜，购买成功！您的卡余额还剩xxx
                current_dateTime = datetime.datetime.now()
                s=stuff+"  "+str(current_dateTime)+"  "+str(1)+"个  "+str(m-0)+" 元"
                mylist.append(s)
                money=money-m-0;
                print("恭喜，购买成功！您的卡余额还剩",money,"元")
            else:
                print("穷鬼，钱不够！请到其他超市购买！")
