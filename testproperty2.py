"'方法伪装成的属性的修改'"
class Person:
    def __init__(self,n):
        self.__name = n  # 私有的属性了
    @property
    def name(self):
        return self.__name

    @name.setter        # 重要程度 ***
    def name(self,new_name):
        if type(new_name) is str:
            self.__name = new_name
        else:
            print('您提供的姓名数据类型不合法')

p = Person('alex')
print(p.name)       #def name(self):
p.name = 'alex_sb' #def name(self,new_name):
print(p.name)       #def name(self):
p.name = 123 #def name(self,new_name):
print(p.name)       #def name(self):