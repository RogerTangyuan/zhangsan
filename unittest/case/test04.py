import unittest

def clear():
    print("开始执行清理函数")
    
    
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.addCleanup(clear)
        print("开始运行测试用例")
    def tearDown(self):
        print("测试用例运行结束")
    
    
    def test_01_demo(self):
        self.doCleanups()
        self.assertEqual(1,2,"判断1和2相等")
        
    def test_02_demo(self):
        self.assertEqual(1,1,"判断1和1相等")


if __name__ == "__main__":
    unittest.main()