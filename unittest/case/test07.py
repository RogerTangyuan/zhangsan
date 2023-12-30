import sys
import os

pythonpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0,pythonpath)

import unittest
import sys
from utils.excelFunc import readExcelData
import ddt

coordinate = {
        "min_row":2,
        "max_row":6,
        "min_col":1,
        "max_col":4
        } 
@ddt.ddt
class TestDemo(unittest.TestCase):    
    
    @ddt.data(*readExcelData("unittest\data\测试数据.xlsx","登录注册",coordinate))
    @ddt.unpack
    def test_01_demo(self,value1,value2,value3,value4):
        self.assertEqual(value3,value4,value2)
        #print(value1,value3,value4)
    

if __name__ == "__main__":
    unittest.main()