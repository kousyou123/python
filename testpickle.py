import pickle
class Animal:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

class Person(Animal):
    def __init__(self, name, hp, atk, sex):
        super().__init__(name, hp, atk)
        self.sex = sex
    # 重写一下内置的双下str，让实例能被print打印出属性
    def __str__(self):
        return str(self.__dict__)

class Dog(Animal):
    def __init__(self, name, hp, atk, kind):
        super().__init__(name, hp, atk)
        self.kind = kind

hero = Person('铁乐', 100, 10, '男')
print(hero)
# 重写双下str后打印出{'sex': '男', 'name': '铁乐', 'atk': 10, 'hp': 100}

# 对象也可以被pickle序列化，这是在内存中操作的示例
ret = pickle.dumps(hero)
print(ret)
# 显示bytes类型的字节：
# b'\x80\x03c__main__\nPerson\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00atkq\x03K\nX\x04\x00\x00\x00nameq\x04X\x06\x00\x00\x00\xe9\x93\x81\xe4\xb9\x90q\x05X\x03\x00\x00\x00sexq\x06X\x03\x00\x00\x00\xe7\x94\xb7q\x07X\x02\x00\x00\x00hpq\x08Kdub.'
res = pickle.loads(ret)
print(type(res), res)
# 重新输出成 <class '__main__.Person'> {'hp': 100, 'atk': 10, 'name': '铁乐', 'sex': '男'}