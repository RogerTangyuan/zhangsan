import unittest

class TestDemo(unittest.TestCase):
    def test_01_demo(self):
        self.assertEqual(1,2,"判断1和2相等")
    def test_02_demo(self):
        self.assertEqual(1,1,"判断1和1相等")
        self.assertTrue(1==1,"判断结果为真")
        self.assertFalse(1!=2,"判断结果为假")
        self.assertIn(1,[1,2])
        a = 1
        b = a
        c = None
        self.assertIs(a,b)
        self.assertIsNot(a,c)
        self.assertIsNone(c)
        #self.assertAlmostEqual(1.112222,1.1234234,2,"前2位小数做对比")
        self.assertAlmostEqual(1.11222,1.12234234,None,"前2位小数做对比",1)

if __name__ == "__main__":
    unittest.main()