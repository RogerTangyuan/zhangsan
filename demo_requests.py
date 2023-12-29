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
