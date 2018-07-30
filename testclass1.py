# 定义一个武器类
class Weapon:
    # 该武器的技能有劈砍
    def cleave(self, target):
        target.hp -= 50 # 劈砍技能对目标造成50点伤害

# 定义一个人类
class Person:
    def __init__(self, name, sex, hp, atk):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.atk = atk
        self.weapon = Weapon() # 给角色绑定一个武器

# 定义一个狗类
class Dog:
    def __init__(self, name, kind, hp, atk):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.atk = atk

# 实例化一个人类角色
tiele = Person('tiele', '男', 30, 10, )
# 实例化一个狗类角色
xiaobai = Dog('小白', '金毛寻回犬', 60, 15)
# 人类装备上武器使用武器技能cleave进行攻击狗类
tiele.weapon.cleave(xiaobai) # 这种用法就叫做组合
print(xiaobai.hp)  # 显示10，表明目标的确hp-50了。