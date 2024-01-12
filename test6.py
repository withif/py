# 定义一个空调类和对应的测试类
class air_conditioner:

    def setBrand(self,brand):
        self._brand=brand
    def getBrand(self):
        return self._brand

    def setPrice(self, price):
        self._price = price

    def getPrice(self):
        return self._price

    def start(self):
        print("空调开机了...")

    def over(self,m):
        print("空调将在",m,"分钟后自动关闭...")




# 打电话业务逻辑
class human:
    # _name=""
    # _sex="male"
    # _age=18
    # _phone_charges=100
    # _phone_brand="小米"
    # _battery_capacity=0.7
    # _phone_screen=6.3
    # _Maximum_standby=18
    # _integral=1100

    def __init__(self,name,sex,age,phonrC,phoneB,batteryC,phoneS,maxS,integral):
        self._name=name
        self._phone_screen=phoneS
        self._age=age
        self._Maximum_standby=maxS
        self._phone_brand=phoneB
        self._phone_charges=phonrC
        self._sex=sex
        self._integral=integral
        self._battery_capacity=batteryC

    def sms(self,content):
        print("短信内容为==》",content)

    def call(self,time,phone_number):
        jifen=0
        feiyong=0
        if(phone_number==""):
            print("号码为空")
            return
        if(self._phone_charges<1):
            print("用户花费小于1元")
            return

        if(int(time)<=10):
            jifen=int(time)*15
            self._integral=self._integral+jifen
            feiyong=int(time)
        elif(int(time)<=20 and int(time)>10):
            jifen=int(time)*39
            self._integral = self._integral + jifen
            feiyong=int(time)*0.8
        else:
            jifen=int(time)*48
            self._integral = self._integral + jifen
            feiyong=int(time)*0.65
        print("此次通话",time,"分钟,","获得",jifen,"积分,","花费",feiyong,"元话费,","剩余",self._phone_charges-feiyong,"话费")



# i.	定义了一个学生类
class student:
    def __init__(self,sno,sname,sage,ssex,stall,sweight,sgrade,saddr,sphone):
            self.no=sno
            self.name=sname
            self.age=sage
            self.sex=ssex
            self.tall=stall
            self.weight=sweight
            self.grade=sgrade
            self.addr=saddr
            self.phone=sphone

    def study(self,time):
        print("学习了",time,"小时")

    def playgame(self,gamename):
        print("正在玩",gamename,"游戏")

    def programming(self,num):
        print("编程写了",num,"行代码")

    def sum(self,*number):
        sum=0
        for i in number:
            sum=sum+i
        return sum

#  ii.	车类  属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。
class car:
    def __init__(self,车型号,车轮数,车身颜色,车重量,油箱存储大小):
            self.车型号=车型号
            self.车轮数=车轮数
            self.车身颜色=车身颜色
            self.车重量=车重量
            self.油箱存储大小=油箱存储大小

    def off_road(self):
        print(self.车型号,"车正在越野")
    def Racing(self):
        print(self.车型号,"车正在竞赛")
    def run(self,func):
        return func


#  笔记本 属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小(Memory size, hard disk size)。  行为：打游戏（传入游戏的名称）,办公。
class notebook:
    def __init__(self,type,time,color,weight,cpu,memory,hard_disk):
        self.type=type
        self.time=time
        self.color = color
        self.weight = weight
        self.cpu = cpu
        self.memory = memory
        self.hard_disk = hard_disk

    def play_games(self,name):
        print("正在打游戏,游戏名称是",name)
    def office(self):
        print("正在办公")

#   猴子 属性：类别，性别，身体颜色，体重
# 行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
class monkey:
    def __init__(self,type,sex,color,weight):
        self.type=type
        self.sex=sex
        self.color=color
        self.weight=weight

    def makefire(self,something):
        print("猴子正在用",something,"造火")

    def study(self,*something):
        for i in something:
            print("猴子正在学习",i,"   ",end="")


































