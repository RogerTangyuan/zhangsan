# print("hello world")  # 字符串
# print(2333)  # 整数
# print(2.33)  # 小数
# print(False) # 布尔值
# print(())  # 元组
# print([])  # 数组
# print({})  # 字典

# print("哈哈",2333,2.333)
# print("哈哈"+"嘻嘻")  # 字符串的拼接
# print("啊哈"*10) #

# 元组
# a = (1,2,3,4,"哈哈","嘻嘻","哈哈",True,False)
# print(a[4])
# print(a[-2])
# print(a[0:4]) # 左闭右开
# print(a[6:])

# print(a.index("哈哈"))  #查找某个值的下标
# print(a.count("哈哈")) #统计某个值的数量

# # 二维元组
# b = (a,"哈哈","嘻嘻")
# print(b[0][3])

# 元组一但写好后不可以修改，而数组可以修改

# 数组
# a = [1,2,3,4,"哈哈","嘻嘻","哈哈",True,False]
# a.append("append") # 往数组中追加数据
# a.insert(2,"insert") # 往数组中指定的位置插入数据
# b = a.pop(5) # 剪切
# print(a)
# print(b)

# # a.clear()
# xx = ["你好","我好"]
# a.extend(xx)
# print(a)


# 字典
# 1、字典中的值没有顺序
# 2、字典必须是键值对结构。 key:value

# a = {"name":"张三",0:"哈哈","age":25}
# print(a["name"])
# a["height"] = "183cm"
# a["name"] = "李斯"
# print(a)

# b = a.get("name") # 使用不存在的键会返回空值
# print(b)

# a.update(name=1111)
# print(a["name"])

# # 数组和字典的删除
# del a["name"]