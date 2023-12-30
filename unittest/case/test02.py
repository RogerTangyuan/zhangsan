import unittest

class TestDemo(unittest.TestCase):
    def test_01_demo(self):
        self.assertEqual(1,2,"判断1和2相等")
    def test_02_demo(self):
        self.assertListEqual([1,2,3],[1,2,3],"判断数组相等")
    @unittest.skip("03这个用例不运行")
    def test_03_demo(self):
        self.assertListEqual([1,2,3],[1,2,4],"判断数组相等")
    @unittest.skipIf(1==1,"结果如果是True，那么这个用例就不会运行")
    def test_04_demo(self):
        self.assertListEqual([1,2,3],[1,2,4],"判断数组相等")
    @unittest.expectedFailure
    def test_05_demo(self):
        self.assertListEqual([1,2,3],[1,2,4],"判断数组相等")    


if __name__ == "__main__":
    unittest.main()