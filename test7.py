# 传入4个键盘输入的数字，并求和。返回打印
def func1():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    return a+b+c+d;


# 编写一个方法，传入一个列表，并求出列表的总和
def func2(list):
    a=0
    for i in list:
        a=a+i
    return a;


# 打印99乘法表
def func3():
    a=9
    for i in range(1,10):
        for j in range(1,10):
            if(i>=j):
                print(j,"*",i,"=",i*j,"  ",end="");
        print("\n")

# 传入一个数字N，然后打印NxN的乘法表
def func4(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i>=j):
                print(j,"*",i,"=",i*j,"  ",end="");
        print("\n")


# 接收一个列表和一个数字，返回这个列表中对应数字的数据，如果数字超出列表长度范围，返回-1
def func5(list,a):
    if(a<len(list)):
        return list[a]
    else:return -1


# 求1~300所有数的和。（方法调用自己完成操作）
def func6(n):
    if(n>0):
        return n+func6(n-1)
    else:return n;


# 1)	求部门员工总共有多少人
def func7(list1,list2,list3):
    a=[]
    for i in list1:
        if i not in a:
            a.append(i)
    for i in list2:
        if i not in a:
            a.append(i)
    for i in list3:
        if i not in a:
            a.append(i)
    return len(a)

# 2)	求只在一个部门存在的人的数量和对应的名字
def func8(list1,list2,list3):
    a=[]
    for i in list1:
        if i not in list2 and i not in list3:
            a.append(i)
    for i in list2:
        if i not in list1 and i not in list3:
            a.append(i)
    for i in list3:
        if i not in list2 and i not in list1:
            a.append(i)
    return a


# 3)	在两个部门以及以上的人员有哪些
def func9(list1,list2,list3):
    a = []
    for i in list1:
        if i  in list2 or i  in list3:
            a.append(i)
    for i in list2:
        if i  in list1 or i  in list3:
            a.append(i)
    for i in list3:
        if i  in list2 or i  in list1:
            a.append(i)
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b


# 编程实现NxN的乘法表的倒叙打印
def func10(n):
    for i in range(n,0,-1):
        for j in range(1,n+1,1):
            if(i>=j):
                print(j,"*",i,"=",i*j,"  ",end="");
        print("\n")