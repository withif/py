import os

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
import unittest

tests =unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")
runner = HTMLTestRunner( # 获取结果运行器对象
 title = "这是测试报告",
 description="这是详细描述",
 verbosity=2, # 报告的详细程度
 stream = open(file="报告.html",mode="w+",encoding="utf-8")
)
runner.run(tests) # 运行并生成测试结果