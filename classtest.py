"测试类的定义及相关操作"
class atestclass:
    def printtest(self,mes):
        print(mes)
        print(self.name)
    def __init__(self, name):
        self.name=name
    def printname(self):
        print("hello {}".format(self.name))
    
