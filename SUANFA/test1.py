from unittest import TestCase
import numpy as np


# 求鞍点
def func1():
    a=[
        [10,14,9,15],
        [7,4,8,10],
        [6,8,4,9],
        [8,52,10,23]
    ]
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            # 获取当前列
            b = (np.array(a))[:, j]
            # print(max(a[i]),end="")
            # print(min(b))
            if(a[i][j]==max(a[i]) and a[i][j]==min(b) ):
               print(a[i][j])
               # print(111)

def func2(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            if(i<=num/2 and j<=num/2):
                if(i>j):
                    print(j,end=" ")
                else:
                    print(i,end=" ")
            elif(i<=num/2 and j>=num/2):
                if((num-j)>=i):
                    print(i,end=" ")
                else:
                    print(num-j+1,end=" ")
            elif(i>=num/2 and j<=num/2):
                if((num-i)>=j):
                    print(j,end=" ")
                else:
                    print(num-i+1,end=" ")
            elif(i>=num/2 and j>=num/2):
                if(i>j):
                    print(num-i+1,end=" ")
                else:
                    print(num-j+1,end=" ")
        print()


# 只能用于正方形
def func3():
    a=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]

    num=1
    cha=len(a)-1
    while(cha>=1):
        for i in range(0,num):
            print(a[i][cha+i],end=" ")
        print()
        cha=cha-1
        num=num+1

    for i in range(0,len(a)):
        print(a[i][i],end=" ")
    print()

    num=len(a)-1
    cha=1
    while(cha<len(a)):
        for i in range(0,num):
            print(a[cha+i][i],end=" ")
        print()
        cha=cha+1
        num=num-1










class Test_test1(TestCase):
    def test_test1(self):
        func1()

    def test_test2(self):
        func2(7)

    def test_test3(self):
        func3()