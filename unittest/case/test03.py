import unittest
def setUpModule():
    print("开始运行测试模块")

def tearDownModule():
    print("测试模块运行结束")    

class TestDemo(unittest.TestCase):
    def setUp(self):
        print("开始运行测试用例")
    def tearDown(self):
        print("测试用例运行结束")
    
    @classmethod
    def setUpClass(cls):
        print("开始运行测试类")
    
    @classmethod
    def tearDownClass(cls):
        print("测试类运行结束")
    
    
    def test_01_demo(self):
        self.assertEqual(1,2,"判断1和2相等")
    def test_02_demo(self):
        self.assertEqual(1,1,"判断1和1相等")


if __name__ == "__main__":
    unittest.main()