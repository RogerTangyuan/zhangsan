import unittest

class TestDemo(unittest.TestCase):
    def test_01_demo(self):
        self.assertEqual(1,2,"判断1和2相等")
    def test_02_demo(self):
        self.assertEqual(1,1,"判断1和1相等")


class TestDemo1(unittest.TestCase):
    def test_01_demo(self):
        self.assertEqual(1,1,"判断1和1相等")
    def test_02_demo(self):
        self.assertEqual(1,1,"判断1和1相等")

if __name__ == "__main__":
    unittest.main()