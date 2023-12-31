# 环境
需要selenium库和浏览器驱动

# 选择元素
## 元素id
html中，如果有id属性，id必须是当前html中唯一的
```
element = wd.find_element(selenium.webdriver.common.by.By.ID,"kw")
```

## 元素class
元素也可以有多个class类型,多个class类型的值之间用空格隔开
我们要用代码选择这个元素，可以指定任意一个class 属性值，都可以选择到这个元素
```
elements = wd.find_elements(selenium.webdriver.common.by.By.CLASS_NAME,"animal")

for element in elements:
    print(element.text)
```

## 标签tag
```
spans = wd.find_elements(selenium.webdriver.common.by.By.TAG_NAME,"span")

for span in spans:
    print(span.text)
```

## 等待元素出现
设置隐式等待语句，如果找不到元素,每隔半秒钟再去界面上查看一次，直到找到该元素，或者过了10秒最大时长
```
wd.implicitly_wait(10)
```


## 输入框
如果输入框中已经有的提示字符，需要先清除掉
```
element.clear()
```

## 获取元素属性
比如要获取元素属性class的值，就可以使用 element.get_attribute('class')

```
element = wd.find_element(By.ID, 'input_name')
print(element.get_attribute('class'))
```

## 获取整个元素对应的html
要获取整个元素对应的HTML文本内容，可以使用element.get_attribute('outerHTML')

如果，只是想获取某个元素内部的HTML文本内容，可以使用element.get_attribute('innerHTML')

## 获取输入框里面的文字
对于input输入框的元素，要获取里面的输入文本，用text属性是不行的，这时可以使用 
```
element = wd.find_element(By.ID, "input1")
print(element.get_attribute('value')) # 获取输入框中的文本
```


## css选择元素
CSS Selector选择class属性元素的语法是在class值前面加上一个点
```
elements = wd.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,".animal")
```

CSS Selector同样可以根据tag名、id属性和class属性来选择元素，
根据tag名选择元素的CSS Selector 语法非常简单，直接写上tag名即可，

比如要选择所有的tag名为span的元素，就可以是这样
```
elements = wd.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,"span")
```
根据id属性 选择元素的语法是在id号前面加上一个井号：#id值

css选择器支持通过任何属性来选择元素，语法是用一个方括号[]
```
element = wd.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,"[href="http://www.miitbeian.gov.cn"]")
```

## 选择子元素和后代元素
直接包含，中间没有其他的层次的元素称为直接子元素，用>连接
```
elements = wd.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,"#container>div")
```

虽然中间隔了几层，但是还是被包含的元素称为后代元素，用空格连接
```
elements = wd.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,"#container div")
```

多组元素同时选择中间用","隔开

## 按次序选择子节点
指定选择的元素 是父元素的第几个子节点
使用 nth-child
例如，选择的是 第2个子元素，并且是span类型
所以这样可以这样写 span:nth-child(2) 

反过来，选择的是父元素的倒数第几个子节点，使用 nth-last-child
比如 p:nth-last-child(1) 就是选择第倒数第1个子元素，并且是p元素


也可以指定选择的元素 是父元素的第几个某类型的子节点
使用 nth-of-type
比如，选择的是第1个span类型的子元素
可以这样写 span:nth-of-type(1)


当然也可以反过来， 选择父元素的 倒数第几个某类型 的子节点
使用 nth-last-of-type

## 兄弟节点
相邻兄弟节点选择
例如h3后面紧跟着的兄弟节点span，这就是一种相邻兄弟关系，可以这样写h3+span

后续所有兄弟节点选择
如果要选择是选择h3后面所有的兄弟节点span，可以这样写h3~span


## frame切换
在html语法中，frame元素或者iframe元素的内部会包含一个被嵌入的另一份html文档
使用WebDriver对象的switch_to属性，像这样
```
wd.switch_to.frame(frame_reference)
```
其中，frame_reference可以是frame元素的属性name或者ID

也可以根据frame的元素位置或者属性特性，使用find系列的方法，选择到该元素，得到对应的WebElement对象
```
wd.switch_to.frame(wd.find_element(By.TAG_NAME, "iframe"))
```
就可以进行后续操作frame里面的元素了


换回原来的主html
```
wd.switch_to.default_content()
```

## 窗口切换
如果我们要到新的窗口里面操作
可以使用Webdriver对象的switch_to属性的window方法
```
wd.switch_to.window(handle)
```

可以通过下面代码获得handle

所谓句柄，大家可以想象成对应网页窗口的一个ID，

那么我们就可以通过 类似下面的代码，
```
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
```

保存当前窗口的句柄
```
mainWindow = wd.current_window_handle
```

## 选择框
radio框选择选项，直接用WebElement的click方法，模拟用户点击就可以了。
```
wd.find_element(By.CSS_SELECTOR,'#s_radio input[value="小雷老师"]').click()
```


对checkbox进行选择，也是直接用 WebElement 的 click 方法，模拟用户点击选择。
```
# 先把 已经选中的选项全部点击一下
elements = wd.find_elements(By.CSS_SELECTOR, 
  '#s_checkbox input[name="teacher"]:checked')

for element in elements:
    element.click()

# 再点击 小雷老师
wd.find_element(By.CSS_SELECTOR, 
  "#s_checkbox input[value='小雷老师']").click()
```

对于Select选择框，Selenium专门提供了一个Select类进行操作

## 其他元素操作方法
比如鼠标右键点击、双击、移动鼠标到某个元素、鼠标拖拽等操作，可以通过Selenium提供的 ActionChains类来实现


## 冻结界面
有些网站上面的元素，我们鼠标放在上面才会显示内容
在开发者工具栏console里面执行如下js代码
```
setTimeout(function(){debugger}, 5000)
```
表示在5000毫秒后，执行debugger命令，界面被冻住

## 弹出对话框
Alert弹出框，目的就是显示通知信息，只需用户看完信息后，点击OK（确定）就可以了

Confirm弹出框，有两个选择供用户选择，分别是OK和Cancel， 分别代表确定和取消操作

Prompt弹出框，是需要用户输入一些信息，提交上去

有些弹窗并非浏览器的alert窗口，而是html元素，这种对话框，只需要通过之前介绍的选择器选中并进行相应的操作就可以了。

# Xpath选择器
## 绝对路径选择
从根节点开始的，到某个节点，每层都依次写下来，每层之间用 / 分隔的表达式，就是某元素的绝对路径
```
elements = driver.find_elements(By.XPATH, "/html/body/div")
```

## 相对路径选择
有的时候，我们需要选择网页中某个元素，不管它在什么位置,需要前面加 //
```
elements = driver.find_elements(By.XPATH, "//div//p")
```

## 通配符
如果要选择所有div节点的所有直接子节点，可以使用表达式 //div/*
```
elements = driver.find_elements(By.XPATH, "//div/*")
for element in elements:
    print(element.get_attribute('outerHTML'))
```

## 根据属性选择
Xpath 可以根据属性来选择元素,是通过这种格式来的 [@属性名='属性值']
### 根据id属性选择
选择 id 为 west 的元素，可以这样 //*[@id='west']

### 根据class属性选择
选择所有 select 元素中 class为 single_choice 的元素，可以这样 //select
[@class='single_choice']

如果一个元素class有多个,对应的 xpath 就应该是 //p[@class="capital huge-city"]

### 根据其他属性
选择具有multiple属性的所有页面元素 ，可以这样 //*[@multiple]

### 属性值包含字符串
要选择 style属性值 包含color字符串的页面元素 ，可以这样 //*[contains(@style,'color')]

要选择 style属性值 以color字符串开头 的页面元素 ，可以这样 //*[starts-with(@style,'color')]

## 按次序选择
### 某类型 第几个 子元素
p类型第2个的子元素 就是 //p[2]

### 第几个子元素
选择父元素为div的第2个子元素，不管是什么类型 //div/*[2]

### 范围选择
选取option类型第1到2个子元素 //option[position()<=2]

选择class属性为multi_choice的前3个子元素 //*[@class='multi_choice']/*[position()<=3]

### 组选择
要选所有的option元素 和所有的 h4 元素，可以使用 //option | //h4


### 选择父节点(css做不到)
某个元素的父节点用 /.. 表示
要选择 id 为 china 的节点的父节点，可以这样写 //*[@id='china']/..


### 兄弟节点选择
选择 后续 兄弟节点，用这样的语法 following-sibling::
要选择 class 为 single_choice 的元素的所有后续兄弟节点 //*[@class='single_choice']/following-sibling::*

### 需要注意的点
要在某个元素内部使用xpath选择元素，需要在xpath表达式最前面加个点
elements = china.find_elements(By.XPATH, './/p')