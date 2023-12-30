import ddt
import unittest

@ddt.ddt
class TestDemo(unittest.TestCase):
    @ddt.data(1,2,3)
    def test_01_demo(self,value):
        self.assertEqual(1,value,"判断1和预期结果相等")
    
    @ddt.data((1,2),(2,2),(3,2))
    @ddt.unpack
    def test_02_demo(self,value1,value2):
        self.assertEqual(value1,value2,"判断1和预期结果相等")
    
    @ddt.data({"name":"张三","age":23},{"name":"李四","age":24},{"name":"李四","age":24})
    @ddt.unpack
    def test_03_demo(self,age,name):
        self.assertEqual(23,age,name)  
    
    @ddt.file_data("data.json")
    @ddt.unpack
    def test_04_demo(self,age,name):
        self.assertEqual(23,age,name) 
    
    @ddt.file_data("data.yaml")
    @ddt.unpack
    def test_05_demo(self,age,name):
        self.assertEqual(23,age,name) 
      
      
if __name__ == "__main__":
    unittest.main()