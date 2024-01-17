import pandas as pd
import pytest


class Test_Calc():
    data = pd.read_excel('1.xlsx')
    @pytest.mark.parametrize("id,a,b,c,real_result,passOrNot,design_basis,test_point",data.values)
    def test_add(self,id,a,b,c,real_result,passOrNot,design_basis,test_point):
        way = test_point[0:2]
        if (way == "加法"):
                if (c == a+b):
                    print("用例通过")
                else:
                    print("用例不通过")
        elif (way == "减法"):
                if (a-b==c):
                    print("用例通过")
                else:
                    print("用例不通过")
        elif (way == "乘法"):
                if (a*b==c):
                    print("用例通过")
                else:
                    print("用例不通过")
        elif (way == "除法"):
                if (c == a//b):
                    print("用例通过")
                else:
                    print("用例不通过")




