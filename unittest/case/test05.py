import unittest
  
class TestDemo(unittest.TestCase):    
    def test_01_demo(self):
        self.assertEqual(1,1,"判断1和1相等")
        
    def test_02_demo(self):
        data = [1,2,3]
        for i in data:
            with self.subTest(data=i):
                self.assertEqual(1,i,"判断1和i相等")


if __name__ == "__main__":
    unittest.main()