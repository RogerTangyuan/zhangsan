import unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
# suite.addTest(TestDemo("test_01_demo"))
# suite.addTest(TestDemo("test_02_demo"))
# suite.addTest(TestDemo1("test_01_demo"))
# suite.addTest(TestDemo1("test_02_demo"))
case = unittest.defaultTestLoader.discover(start_dir="D:/workhome/github/zhangsan/unittest",pattern="test*.py")
suite.addTest(case)

with open ("测试报告.html","wb",) as f:
    runner = HTMLTestRunner(stream=f,title="测试报告",description="这是项目的描述")
    runner.run(suite)