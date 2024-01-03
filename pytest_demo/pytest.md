# 测试用例代码
首先，我们编写的测试用例代码文件， 必须以 test_ 开头，或者以 _test 结尾
```
class Test_错误密码:

    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1
        
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2
        
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2
```

如果我们把测试用例存放在类中， 类名必须以 Test 为前缀的 类 ，用例对应的方法必须以 test 为前缀的方法。


pytest 中用例的检查点 直接用 Python 的 assert 断言。

assert 后面的表达式结果 为 True ，就是 检查点 通过，结果为False ，就是检查点 不通过。

# 产生报告
```
pytest pytest_demo --html=pytest_demo\report.html --self-contained-html
```
这样就会产生名为 report.html 的测试报告文件，可以在浏览器中打开


# 初始化、清除
## 模块级别
模块级别 的初始化、清除分别在整个模块的测试用例执行前后执行，并且只会执行1次 。
定义 setup_module 和 teardown_module 全局函数
```
def setup_module():
    print('\n *** 初始化-模块 ***')


def teardown_module():
    print('\n ***   清除-模块 ***')

class Test_错误密码:

    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1
        
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2
        
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2


class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
        
    def test_C001022(self):
        print('\n用例C001022')
        assert 2 == 2
```

## 类级别
类级别 的初始化、清除分别在整个类的测试用例执行前后执行，并且只会执行1次
如下定义 setup_class 和 teardown_class 类方法
```
def setup_module():
    print('\n *** 初始化-模块 ***')

def teardown_module():
    print('\n ***   清除-模块 ***')

class Test_错误密码:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')
        
    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1
        
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2
        
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2

class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
        
    def test_C001022(self):
        print('\n用例C001022')
        assert 2 == 2
```

## 方法级别
方法级别 的初始化、清除分别在类的每个测试方法执行前后执行，并且每个用例分别执行1次
如下定义 setup_method 和 teardown_method 实例方法
```
def setup_module():
    print('\n *** 初始化-模块 ***')

def teardown_module():
    print('\n ***   清除-模块 ***')

class Test_错误密码:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')
        
    def setup_method(self):
        print('\n --- 初始化-方法  ---')

    def teardown_method(self):
        print('\n --- 清除  -方法 ---')
        
    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1
        
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2
        
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2

class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
        
    def test_C001022(self):
        print('\n用例C001022')
        assert 2 == 2
```

## 目录级别
目标级别的 初始化清除，就是针对整个目录执行的初始化、清除。
我们在需要初始化的目录下面创建 一个名为 conftest.py 的文件，里面内容如下所示
```
import pytest 

@pytest.fixture(scope='package',autouse=True)
def st_emptyEnv():
    print(f'\n#### 初始化-目录甲')
    yield
    
    print(f'\n#### 清除-目录甲')
```

# 挑选用例执行
## 指定一个模块
pytest pytest_demo\cases\test_错误登录.py

## 指定目录
pytest pytest_demo

## 指定模块里面的函数或类
pytest pytest_demo\cases\test_错误登录.py::Test_错误密码

pytest pytest_demo\cases\test_错误登录.py::Test_错误密码::test_C001001

## 根据名字
可以使用 命令行参数 -k 后面加名字来挑选要执行的测试项
pytest -k C001001 -s
pytest -k "not C001001" -s
pytest -k "错 and 密码2" -s
pytest -k "错 or 密码2" -s


## 根据标签
可以这样给 某个方法加上标签 webtest
```
import pytest

class Test_错误密码2:

    @pytest.mark.webtest
    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
```
然后，可以这样运行指定标签的用例

pytest cases -m webtest -s

