import time

# 需求：用户登录度小满家庭记账系统（管理员账户：admin/123456,普通用户:lisi/123456），若满足三次之内登录成功,进度进入家庭记账界面。若管理登录成功，可对用户的日常理财流程进行打印
def func1():
    a = zhangwu(1, "吃饭支出", "交通银行", 247.0, "2016-03-02", "家庭聚餐")
    b = zhangwu(2, "工资收入", "现金", 12345.0, "2016-03-02", "开工资了")
    c = zhangwu(3, "服装支出", "现金", 1998.0, "2016-03-02", "买衣服")
    d = zhangwu(4, "吃饭支出", "现金", 325.0, "2016-03-02", "朋友聚餐")
    e = zhangwu(5, "股票收入", "工商银行", 8000.0, "2016-03-02", "股票大涨")
    f = zhangwu(6, "股票收入", "工商银行", 5000.0, "2016-03-02", "股票大涨")
    g = zhangwu(7, "工资收入", "交通银行", 5000.0, "2016-03-02", "开工资了")
    h = zhangwu(8, "礼金支出", "现金", 5000.0, "2016-03-02", "朋友结婚")
    i = zhangwu(9, "其他支出", "现金", 1560.0, "2016-03-02", "丢钱了")
    j = zhangwu(10, "交通支出", "交通银行", 2300.0, "2016-03-02", "油价上涨")
    k = zhangwu(11, "吃饭支出", "工商银行", 1000.0, "2016-03-02", "吃饭")
    l = zhangwu(12, "工资收入", "现金", 1000.0, "2016-03-02", "开资")
    m = zhangwu(13, "交通支出", "现金", 2000.0, "2016-03-02", "机票好贵")
    n = zhangwu(14, "工资收入", "现金", 5000.0, "2016-03-02", "又开资")
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)
    list.append(e)
    list.append(f)
    list.append(g)
    list.append(h)
    list.append(i)
    list.append(j)
    list.append(k)
    list.append(l)
    list.append(m)
    list.append(n)



    m=[]
    n=[]
    for i in list:
        m.append(i.type)
    print("请输入账号")
    a=str(input())
    print("请输入密码")
    b = str(input())
    if(a=="admin" and b=="123456"):
       #        管理员
       # print("管理员")
       while(1):
           print("1.添加财务 2.编辑财务 3.删除财务 4.查询财务 5退出系统")
           print("请输入要操作的功能序号【1-5】")
           caozuo = str(input())
           if (caozuo == "1"):
               print(1)
               print("请输入类别")
               aa=str(input())
               print("请输入账户")
               bb = str(input())
               print("请输入金额")
               cc = str(input())
               print("请输入说明")
               dd = str(input())
               date_str = time.strftime('%Y-%m-%d', time.localtime())
               exam=zhangwu(len(list)+1,aa,bb,cc,str(date_str),dd)
               list.append(exam)
               print("添加成功")
           elif (caozuo == "2"):
               print(2)
               print("请输入要编辑的id")
               mm=str(input())
               for i in list:
                   if(str(i.id)==mm):
                       print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format("ID", "类型", "账户", "金额",
                                                                                           "时间",
                                                                                           "说明", chr(12288)))
                       print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format(i.id, i.type, i.account,
                                                                                           i.money,
                                                                                           i.time, i.instruction),
                             chr(12288))
                       print("请输入类别")
                       aa = str(input())
                       print("请输入账户")
                       bb = str(input())
                       print("请输入金额")
                       cc = str(input())
                       print("请输入说明")
                       dd = str(input())
                       list.remove(i)
                       date_str = time.strftime('%Y-%m-%d', time.localtime())
                       exam = zhangwu(int(mm), aa, bb, cc, str(date_str), dd)
                       list.append(exam)
                       print("修改成功")
                       break
               print("未找到id对应的记录")
           elif (caozuo == "3"):
               print("请输入要删除的id")
               dele=str(input())
               aa=0
               for i in list:
                   if(str(i.id)==dele):
                       list.remove(i)
                       aa=1
               if(aa==1):
                   print("id为",dele,"已删除")
               else:
                   print("未找到id为",dele,"的记录")
           elif (caozuo == "4"):
               print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format("ID", "类型", "账户", "金额", "时间",
                                                                                   "说明", chr(12288)))
               for i in list:
                   print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format(i.id, i.type, i.account, i.money,
                                                                                       i.time, i.instruction),chr(12288))
           elif (caozuo == "5"):
               print("感谢使用")
               break
           else:
               print("请输入正确的指令")
    elif(a=="lisi" and b=="123456"):
       # 用户
      while(1):
          print("1.查询所以 2.按条件查询 3.q退出")
          c = str(input())
          if (c == "1"):
              print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format("ID", "类型", "账户", "金额", "时间",
                                                                                  "说明", chr(12288)))
              for i in list:
                  print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format(i.id, i.type, i.account, i.money,
                                                                                      i.time, i.instruction),
                        chr(12288))
          elif (c == "2"):
              print("请输入类别")
              d = str(input())
              if d not in m:
                  print("没有此类型")
              else:
                  print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format("ID", "类型", "账户", "金额",
                                                                                      "时间",
                                                                                      "说明", chr(12288)))
                  for i in list:
                      if (i.type == d):
                          print('{0:^10}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}\t{5:^20}'.format(i.id, i.type, i.account,
                                                                                              i.money, i.time,
                                                                                              i.instruction),
                                chr(12288))
          elif(c=="q"):
              print("感谢使用")
              break
          else:
              print("请输入正确的编号")
    else:
       print("用户名或密码错误")

class zhangwu:
    def __init__(self, id, type,account,money,time,instruction):
        self.id = id
        self.type=type
        self.account=account
        self.money=money
        self.time=time
        self.instruction=instruction

