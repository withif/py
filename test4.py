# 开户
import random

class user:
    def __init__(self, num, name, pwd, addr, money, bank):
        self.num = num
        self.name = name
        self.pwd = pwd
        self.addr = addr
        self.money = money
        self.bank = bank

def add_user(user,list):
    num=0
    if(len(list)>=100):
        print("用户库已满")
        return 3
    else:
        for i in list:
            if(i.name==user.name):
                print("用户已存在")
                return 2
            num=num+1
        if(num==len(list)):
            list.append(user)
            return 1

# 存钱
def savemoney(list,num,money) -> bool:
    n=0
    for i in list:
        if(str(i.num)==str(num)):
            list.remove(i)
            i.money=i.money+money
            list.append(i)
            return True
        n=n+1
        if(n==len(list)):
            return False

# 取钱
def withdraw_money(num,pwd,money,list):
    for i in list:
        if(str(i.num)==str(num) ):
            if( str(pwd)==str(pwd)):
                if(i.money>=money):
                    list.remove(i);
                    i.money = i.money - money
                    list.append(i);
                    print("取钱成功,您的账户信息如下")
                    print("当前账号：", i.num, ",密码:", i.pwd, ",余额：", i.money, "元，用户居住地址：", i.addr,
                          "，当前账户的开户行：", i.bank, ".")

                    return
                else:
                    print("账户余额不足")
                    return 3
            else:
                print("密码错误")
                return 2
        print("用户名不存在")
        return 1

# 转账
def transfer_money(fnum,tnum,pwd,money,list):
    num=[]
    for i in list:
        if(str(i.num)==str(fnum)):
            num.append(i)
            if(str(i.pwd)!=str(pwd)):
                return 2
        if(str(i.num)==str(tnum)):
            num.append(i)
    if(len(num)!=2):
        return 1
    if(str(num[0].num)==str(fnum)):
        if(num[0].money>money):
            list.remove(num[0])
            num[0].money=num[0].money-money
            list.append(num[0])

            list.remove(num[1])
            num[1].money = num[1].money + money
            list.append(num[1])
        else:
            return 3

    if (str(num[1].num) == str(fnum)):
        if (num[1].money > money):
            list.remove(num[1])
            num[1].money = num[1].money - money
            list.append(num[1])

            list.remove(num[0])
            num[0].money = num[0].money + money
            list.append(num[0])
        else:
            return 3


# 5.	查询账户功能
def select_account(num,pwd,list):
    a=0
    for i in list:
        if(str(i.num)==str(num)):
            if(str(i.pwd)==str(pwd)):
                a=a+1
                print("当前账号：",i.num,",密码:",i.pwd,",余额：",i.money,"元，用户居住地址：",i.addr,"，当前账户的开户行：",i.bank,".")
            else:
                print("密码错误")
    if(a!=1):
        print("该用户不存在")


# 中国工商银行账户管理系统
def start(list):

    while(1):
        print("*************************************************************************")
        print("*                         中国工商银行                                     ")
        print("                          账户管理系统                                     ")
        print("                             V1.0                                        ")
        print("*************************************************************************")
        print("                                                                         ")
        print("1.开户                                                                    ")
        print("2.存钱                                                                    ")
        print("3.取钱                                                                    ")
        print("4.转账                                                                    ")
        print("5.查询                                                                    ")
        print("6.BYE                                                                    ")
        print("*************************************************************************")
        print("请输入操作")
        a=str(input())
        if(a=="1"):
            a = random.randint(10000000, 99999999)
            addr1 = "中国北京市昌平区88号"
            print("请输入姓名")
            aa=str(input())
            print("请输入密码")
            bb = int(input())
            print("请输入地址")
            cc = str(input())
            i = user(a, aa, str(bb), cc, 0, "中国工商银行的昌平支行")
            add_user(i,list)
            print("开户成功")
            print("当前开户账号：", i.num, ",密码:", i.pwd, ",余额：", i.money, "元，用户居住地址：", i.addr,
                  "，当前账户的开户行：", i.bank, ".")
        elif(a=="2"):
            print("请输入用户的账号")
            aa = str(input())
            print("请输入金额")
            money = int(input())
            savemoney(list,aa,money)
        elif(a=="3"):
            print("请输入用户的账号")
            aa = str(input())
            print("请输入用户的密码")
            bb = str(input())
            print("请输入金额")
            money = int(input())
            withdraw_money(aa,bb,money,list)
        elif(a=="4"):
            print("请输入你的账号")
            f = str(input())
            print("请输入他的账号")
            t = str(input())
            print("请输入用户的密码")
            bb = str(input())
            print("请输入金额")
            money = int(input())
            transfer_money(f,t,bb,money,list)
        elif(a=="5"):
            print("请输入他的账号")
            aa = str(input())
            print("请输入用户的密码")
            bb = str(input())
            select_account(aa,bb,list)
        elif(a=="6"):
            print("感谢使用")
            break
        else:
            print("请输入正确的指令")









