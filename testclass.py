import classtest
import testduixiang

a=classtest.atestclass("kevin")
a.printtest("aaa")
a.printname()

bus1 = testduixiang.HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)
bus2 = testduixiang.HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = testduixiang.HauntedBus()#bus3 一开始也是空的， 因此还是赋值默认的列表。
print(bus3.passengers) #但是默认列表不为空！
bus3.pick('Dave')
print(bus2.passengers) # 登上 bus3 的 Dave 出现在 bus2 中。
print(bus2.passengers is bus3.passengers) #问题是， bus2.passengers 和 bus3.passengers 指代同一个列表
print(bus1.passengers) #但 bus1.passengers 是不同的列表。
# 问题在于， 没有指定初始乘客的 HauntedBus 实例会共享同一个乘客列
# 表.出现这个问题的根源是， 默认值在定义函数时计算（通
# 常在加载模块时） ， 因此默认值变成了函数对象的属性。 因此， 如果默
# 认值是可变对象， 而且修改了它的值， 那么后续的函数调用都会受到影响。


