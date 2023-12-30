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
case = unittest.defaultTestLoader.discover(start_dir="unittest\case",pattern="test*.py")
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

case = unittest.defaultTestLoader.discover(start_dir="unittest\case",pattern="test*.py")
suite.addTest(case)

with open ("测试报告.html","wb",) as f:
    runner = HTMLTestRunner(stream=f,title="测试报告",description="这是项目的描述")
    runner.run(suite)
```


# 断言
## 常用的断言
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

## 比较断言
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

## 装饰器
在实际工作中，用例可能会存在很多。
但是这些用例，有可能不是所有的用例都是需要运行的。
利用testCase自带的装饰器来实现用例运行的过程的控制

- @unittest.skip("03这个用例不运行")
控制对应的的用例不参与测试的过程，这条用例是不运行的
- @unittest.skipIf(1==1,"结果如果是True，那么这个用例就不会运行")
如果条件为真，那么这个用例不会参与运行
- @unittest.skipUnless()
如果条件为假，那么这个用例不会参与运行
- @unittest.expectedFailure
我们在测试之前已知这个用例是无法通过测试的
加上这个装饰器，那么这个用例在测试的时候就算没有通过测试，也不算失败

运行结果说明
\.表示测试通过
F 表示测试失败
s 表示跳过测试
x 表示预期失败
u 表示意外成功

## 测试夹具（fixture）
测试夹具可以把我们在测试运行前和结束后需要运行的代码抽离出来，单独放到夹具中去运行
可以方便我们的代码组织和维护，减少重复的代码量


- setUp
在没事测试用例运行前运行，一般我们会在这里写一些实现测试用例的前置条件的代码
- tearDown
在每个测试用例运行结束后，一般我们会在这里面写一些清理测试环境的代码，或者关闭，删除某个测试中出现不必要的东西的代码

- setUpClass
在每个测试类运行前运行

- setDownClass
在每个测试类结束运行的时候运行

- setUpModule
在每个测试模块运行前运行
- tearDownModule
在每个测试模块运行结束后运行


## unittest的清理函数
清理函数addCleanup和doCleanups是python3.1后新加的功能
清理函数默认都是在teardown后面运行的

清理函数的使用，需要先自己封装一个方法，这个方法里面写的代码就是用来做清理的作用的

可以在测试类的任意位置，注册清理函数
self.addCleanup(clear)
如果addCleanup写在setUp中，那么这个清理函数会对所有的用例teardown后生效
我们可以通过doCleanups方法来控制我们的清理函数运行的位置

在python3.9后新增了addClassCleanup和doClassCleanups用于测试类的方法

清理函数和夹具
相同点，都可以实现对测试用例，测试类的前置、后置的操作处理
不同点，清理函数可以自定义使用的位置，比较灵活


## unittest子测试
使用subTest可以让我们的测试用例支持数据驱动的测试方式
写法固定
```py
def test_01_demo(self):
    data = (1,2,3) #可以从文件中读取数据
    for d in data:
        with self.subTest(data=d):
            self.assertEqual(1.d)
```

## unittest的数据驱动的常规实现的过程
subTest 对应其他格式的测试数据文件，需要自己封装方法来读取
ddt 第三方包，通过ddt类装饰器调用
@ddt.file_data 可以实现自动的从文件中去读取测试数据,json,yaml(该格式需要安装PyYaml包),但是对应其他格式的测试数据文件，需要自己封装方法来读取
#@data(test_data)不加*，是一条用例，执行1次。输出结果：item [do, 3]。加了*，@data(*test_data)，
#就脱1层外套变成两个数据，运行两次，两条用例。
#输出结果：item do
#         item 3


## 邮件发送
1、准备工作
以网易163邮箱为例，我们需要在我们自己的邮箱中开启smtp的功能，生成密钥
2、开始编写代码

## 展望
1、结合实际项目，去封装更多更好的方法到我们的框架中。
比如，结合接口自动化测试的项目，我们可以把requests给封装起来，方便我们快速的操作接口。
封装pyMysql，实现对mysql数据库的快速操作。
做UI自动化测试。
实现OP，把要操作的测试对象给封装起来，它selenium做二次的封装。

2、消息推送
邮件、微信、钉钉、短信

3、持续集成
把测试过程继承到Jenkins
