"""
class 声明类的名字
类的名字首字母必须大写
类里面所有的方法，都必须传一个self参数
"""


class GirlFriend():
    """
    女朋友
    """
    def __init__(self,sex,height,weight,hair,age):
        self.sex = sex
        self.height = height
        self.weight = weight
        self.hair = hair
        self.age = age
    
    def caiyi(self,num):
        """
        才艺
        """
        if num == 1:
            print("唱跳rap篮球")
        elif num == 2:
            print("code两年半")
        else:
            print("开挖掘机")
    
    def chuyi(self):
        """
        厨艺
        """
        print("辣椒炒肉")

"""
继承
重写
"""        
class Nvpengyou(GirlFriend):
    def chuyi(self):
        print("红烧肉")
        
# 实例化
zhangsan = Nvpengyou("女","166cm","55kg","长发","18岁")
zhangsan.caiyi(1)
zhangsan.chuyi()
print(zhangsan.height)