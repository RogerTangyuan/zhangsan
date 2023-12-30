# TestCase
```py
import unittest

class TestDemo(unittest.TestCase):
    def test_01_demo(self):
        self.assertEqual(1,2,"判断1和2相等")
    def test_02_demo(self):
        self.assertEqual(1,1,"判断1和1相等")

if __name__ == "__main__":
    unittest.main()
```

使用unittest编写测试用例，必须使用测试类类进行
在测试类里面的方法就是我们的测试用例了
测试用例的方法必须是test开头的才可以
unittest.main()会自动发现我们这个模块中的所有测试类中的测试用例
在测试用例的方法中，我们可以使用TestCase自带的断言功能来实现对预期结果和实际结果的判断


# TestSuite
我们可以使用测试套件，把不同的测试用例都加载到测试套件中
然后通过直接运行测试套件，就可以实现不同模块的测试用例了

```
suite = unittest.TestSuite()
case = unittest.defaultTestLoader.discover(start_dir="D:/workhome/github/zhangsan/unittest",pattern="test*.py")
suite.addTest(case)
```

使用unittest.defaultTestLoader.discover方法可以实现在指定文件夹中自动发现我们的测试用例。
start_dir,指定测试用例所在的文件夹
pattern,测试用例的py模块的命名规则
最后使用suite.addTest的方法把发现的用例加载到测试套件中。

# 运行套件和生成测试报告
unittest自带的测试白宫是文本格式的，可读性不是很好,所以一般使用第三方的模块来生成测试报告。
# HTMLTestRunner类里
stream,把测试报告的文件流保存到哪个文件中
title,测试报告的名字
description,测试报告的详细描述

```py
import unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()

case = unittest.defaultTestLoader.discover(start_dir="D:/workhome/github/zhangsan/unittest",pattern="test*.py")
suite.addTest(case)

with open ("测试报告.html","wb",) as f:
    runner = HTMLTestRunner(stream=f,title="测试报告",description="这是项目的描述")
    runner.run(suite)
```


# 断言
# 常用的断言
- assertEqual
判断任意的两个值相等
- assertNotEqual
判断两个值不相等
- assertTrue
判断结果为真
- assertFalse
判断结果为假
- assertIn
判断任意的一个值是否在某个范围内
- assertNotIn
判断任意的一个值不在某个范围内
- assertIs
判断任意的两个对象属于同一个对象
- assertIsNot
判断任意的两个对象不是同一个对象
- assertIsNone
判断某个值为空
- assertIsNotNone
判断某个值不为空
- assertIsInstance
判断某个对象属于某个class实例
- assertNotIsInstance
判断某个对象不属于某个class实例

# 比较断言
- assertAlmostEqual
判断两个小数约等于
这个断言方法存在5个参数
first，需要判断的第一个值
second，需要判断的第二个值
places，只比较前几位小数，默认7位
msg，
delta，不能和places同时存在，它的作用是限制做对比的两个值，他们的差值必须小于delta

assertAlmostEqual(1.112222,1.1234234,2,"前2位小数做对比")
assertAlmostEqual(1.11222,1.12234234,None,"前2位小数做对比"，1)

- assertGreater
first > second