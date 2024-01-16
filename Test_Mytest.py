import math
from unittest import TestCase

import pytest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
import yaml

class TestCalc:

    def setup_method(self):         # 函数执行之前执行
        print("函数级别前加载")
    def teardown_method(self):      # 函数执行之后执行
        print("函数级别后加载")
    def setup_class(self):          # 类执行之前执行
        print("类级别的前加载")
    def teardown_class(self):       # 类执行之后执行
        print("类级别的后加载")
    def testAdd1(self):
        a = 6
        b = 5
        c = 11
        assert (a+b) == c
    def testAdd2(self):
        a = 6
        b = 5
        c = 11
        assert (a+b) == c

    f = open(file="data.yaml", mode="r", encoding="utf-8")
    data = yaml.load(f, Loader=yaml.SafeLoader)
    def test_Add(self):
        f=open(file="data.yaml",mode="r",encoding="utf-8")
        data=yaml.load(f,Loader=yaml.SafeLoader)
        # print(type(data))            # 得到一个list
        result_dict = {key_value.split(':')[0]: int(key_value.split(':')[1])
                       for item in data for key_value in item.split()}      # ['a:1 b:2 c:3', 'a:4 b:4 c:8']
        print(type(result_dict))
        res=result_dict.get("a")+result_dict.get("b")
        assert res==result_dict.get("c")

    @pytest.mark.parametrize("a,b,c",data)
    def test_Add2(self,a,b,c):
        sun=a+b
        c=c
        assert c==sun