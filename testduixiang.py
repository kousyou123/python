class HauntedBus:
    """备受幽灵乘客折磨的校车"""
    def __init__(self, passengers=[]): # 如果没传入 passengers 参数， 使用默认绑定的列表对象， 一开始是空列表。
        self.passengers = passengers  #这个赋值语句把 self.passengers 变成 passengers 的别名， 而没有传入 passengers 参数时， 后者又是默认列表的别名。
    def pick(self, name):
        self.passengers.append(name) #在 self.passengers 上调用 .remove() 和 .append() 方法时， 修改的其实是默认列表， 它是函数对象的一个属性。
    def drop(self, name):
        self.passengers.remove(name)


class TwilightBus:
    """让乘客销声匿迹的校车"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = [] #这里谨慎处理， 当 passengers 为 None 时， 创建一个新的空列表。
        else:
            self.passengers = passengers #然而， 这个赋值语句把 self.passengers 变成 passengers 的别名， 而后者是传给 __init__ 方法的实参
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)  #在 self.passengers 上调用 .remove() 和 .append() 方法其实会修改传给构造方法的那个列表。

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name) 
