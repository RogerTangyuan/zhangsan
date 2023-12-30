import unittest
import time
from utils import HTMLTestRunner
suite = unittest.TestSuite()

#case = unittest.defaultTestLoader.discover(start_dir="unittest\case",pattern="test*.py")
case = unittest.defaultTestLoader.discover(start_dir="unittest\case",pattern="test07.py")
suite.addTest(case)
now = time.strftime("%Y-%m-%d %H-%M-%S")
path = "unittest/reports/测试报告-{}.html".format(now)
with open (path,"wb",) as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="测试报告",description="这是项目描述")
    runner.run(suite)