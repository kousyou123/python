"'方法伪装成的属性的删除'"
class Person:
    def __init__(self,n):
        self.__name = n  # 私有的属性
    @property            # 重要程度 ****
    def name(self):
        return self.__name
    @name.deleter
    def name(self):
        print('name 被删除了')
    @name.deleter         # 重要程度*
    def name(self):
        del self.__name

p = Person('alex')
print(p.name)
del p.name  # 只是执行了被@name.deleter装饰的函数
print(p.name)