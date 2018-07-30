class BirthDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

class Teacher:
    def __init__(self, name, sex, birth, course):
        self.name = name
        self.sex = sex
        self.birth = birth
        self.course = course

# 实例化一个老师的同时，传参的时候还可以传另一个实例化的对象
tiele = Teacher('铁乐', '男', BirthDate(1999, 4, 1), Course('python', '19800', '5 months'))
# 查看时可以直接用组合的方式查看
print(tiele.course.name, tiele.birth.year)  # python 1999
print(tiele.course.price, tiele.birth.month) # 19800 4