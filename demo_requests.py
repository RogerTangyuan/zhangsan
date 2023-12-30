import requests
# requests有2种请求方式：
# 1、request方法，适用于所有类型的请求。
# 2、requests封装好的，专门用于对应的请求类型的方法，比如get/post/head/put/delete/patch/options


# request:请求类型和请求地址的参数是必填参数，并且必须是字符串格式
# r = requests.request("get","https://www.baidu.com")
# print(r.text)

# 其他对应类型的方法：必填参数只有请求地址
# r = requests.get("https://www.baidu.com")
# print(r.text)

# 接口的结构
# 请求
# url 请求地址
# methods 请求类型，常见的请求类型，get/post/head/put/delete/patch/options
# headers 请求头，包含了客户端信息以及用来鉴权的内容
# data 请求数据

# 响应
# headers 响应头，包含了服务端的信息
# status_code 状态码，http的状态码，常见的就是200、400、404、405、500
# data 响应数据，接口返回的数据


# 请求参数
# params，字典，主要用于get类型的请求数据

# data，字典(表单类型数据)/json/字符串，主要用于post类型的表单格式的请求数据

# method = "get"
# url = "http://119.45.233.102:6677/testgoup/test/list"
# params = {
#     "name":"张三",
#     "age":23
# }

# r = requests.request(method,url,params=params)
# print(r.text)

# url = "http://119.45.233.102:6677/testgoup/test/list?name=张三&age=23"


# r = requests.request(method,url)
# print(r.text)

# method = "post"
# url = "http://119.45.233.102:6677/testgoup/test/form"
# data = {
#     "name":"张三",
#     "age":23
# }

# r = requests.request(method,url,data=data)
# print(r.text)


# json,字典，用于post类型接口的json格式的请求数据
# method = "post"
# url = "http://119.45.233.102:6677/testgoup/test/json"
# data = {
#     "name":"张三",
#     "age":23
# }
# r = requests.request(method,url,json=data)
# print(r.text)


# files,用于文件的上传
# method = "post"
# url = "http://119.45.233.102:6677/testgoup/test/upload"
# data = {"files":open("日记.txt","rb")}
# r = requests.request(method,url,files=data)
# print(r.text)


# 文件下载
# stream为false，就一次性下载全部文件，适用于小文件的下载
# stream为true，就可以一点点下载文件，适用于大文件的下载
# url = "http://119.45.233.102:6677/testgoup/test/download"
# method = "get"
# r = requests.request(method,url,stream=True)

# with open("图片.png","wb") as f:
#     for chunk in r.iter_content(chunk_size=512):
#         f.write(chunk)


# cookies操作
# 主要用于接口鉴权，一般再登录接口会返回cookies，然后其他的要求登陆后才能使用的接口需要cookies对应的参数，从而实现登录的鉴权

# 登录
# url = "http://119.45.233.102:6677/testgoup/test/login"
# method = "post"
# json = {"username":"admin","password":"123456"}
# r = requests.request(method,url,json=json)
# print(r.headers.get("Set-Cookie"))

# # 获取信息
# url = "http://119.45.233.102:6677/testgoup/test/info"
# method = "get"
# cookies = {"token":"sdjhfsdjkfsdkfjseiufseiuf"}
# r =requests.request(method,url,cookies=cookies)
# print(r.text)

# 会话保持
# 使用的请求对象不是request，而使用session的对象，两者使用方式是一样的
# s = requests.session()
# url = "http://119.45.233.102:6677/testgoup/test/login"
# method = "post"
# json = {"username":"admin","password":"123456"}
# r = s.request(method,url,json=json)
# print(r.headers.get("Set-Cookie"))

# # 获取信息
# url = "http://119.45.233.102:6677/testgoup/test/info"
# method = "get"
# r =s.request(method,url)
# print(r.text)


# auth
# 是一种对接口进行鉴权的方式，与cookies和token的作用差不多
# url = "http://119.45.233.102:6677/testgoup/test/auth"
# method = "post"
# auth =("admin","123456")
# r = requests.request(method,url,auth=auth)
# print(r.text)

# 响应数据
# text
# 以文本的格式读取响应的数据
# content
# 以二进制字节的方式读取响应的数据
# headers
# 响应头
# url
# 请求的地址

# 钩子函数
# hook指我们可以定义一盒或者多个公共方法，让请求结束后，自动去调用这些公共方法
# def readText(r,*args,**kwargs):
#     """
#     在接口请求结束后自动打打印text属性
#     """
#     print(r.text)
    
# def readHeaders(r,*args,**kwargs):
#     """
#     在接口请求结束后自动打印响应头属性
#     """
#     print(r.headers)

# method = "post"
# url = "http://119.45.233.102:6677/testgoup/test/json"
# data = {
#     "name":"张三",
#     "age":23
# }
# r = requests.request(method,url,json=data,hooks=dict(response=[readText,readHeaders]))

