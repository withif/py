import random

# 详细业务需求
# 1.	系统随机产生一个随机数
# 2.	用户从键盘输入猜的数字
# a)	系统判断数字是否比系统产生的大，若大了，则友好提示：大了
# b)	若小了，则提示小了
# c)	否则，则提示：恭喜猜中，本轮幸运数字：xxx
# 技术选型：
# 1.	随机数：random
# 2.	输入：input
# 3.	判断：if…elif…elif…else
# 4.	循环：while,for循环

def  func1():
        a = random.randint(1,100)
        b = int(input())
        while (1):
                if (a < b):
                        print("大了")
                elif (a > b):
                        print("小了")
                else:
                        print("恭喜猜中，本轮幸运数字：", a);break
                b = int(input())



# 1.	在基于1.0版本的需求之上，添加新需求
# 玩家起始有5000金币，每猜错一次扣500金币，猜对了即奖励3000金币，游戏结束
# 一直到本金余额不足为止。游戏退出

def  func2(money):

        a = random.randint(1, 100)
        b = int(input())
        while (1):
                if (a < b):
                        print("大了")
                        money=money-500
                elif (a > b):
                        print("小了")
                        money = money - 500
                elif(a==b):
                        print("恭喜猜中，本轮幸运数字：", a);
                        money = money + 3000;
                        # print("随机数已重置")
                        # func2()

                if(money<=0):
                        print("本金不足")
                        break

                b = int(input())



# 在1.0或者2.0 的基础上添加一个新功能：
# 	玩家在猜中后，系统需要询问玩家是否继续下一轮游戏。
# 	若继续：则继续下一轮。并重新生成一个随机数字。
# 	否则，系统退出。

def func3(money):

        a = random.randint(1, 100)
        b = int(input())
        while (money>0):
                if (money <= 0):
                        print("本金不足")
                        break
                if (a < b):
                        print("大了")
                        money = money - 500
                elif (a > b):
                        print("小了")
                        money = money - 500
                elif (a == b):
                        print("恭喜猜中，本轮幸运数字：", a);
                        money = money + 3000;
                        print("是否继续下一轮游戏：yes/no?")
                        while(money>0):
                                answer = input()
                                if ("yes" == answer):
                                        print("随机数已重置")
                                        func3(money)
                                elif ("no" == answer):
                                        print("感谢使用")
                                        break
                                else:print("请输入yes或者no");
                        break
                b = int(input())
                if (money <= 0):
                        print("本金不足")
                        break