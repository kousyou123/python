tu=(1,2,3)
print(tu)
tut=[2,3,4]
tu1=([1,2,3],["a","b"])
print(tu1)
tu2=tu1[0].append(4)#元组中数据不能改变
print(tu2)

s=[1,2,2,4,4,6,7]
s1=set(s)#集合可以去除重复数据
s2=list(s1)
print(s2)

s3={1,3,4,6,7}
s4={3,4,8,9}
s5=s3&s4 #交集
print(s5)
s6=s3|s4#并集
print(s6)
s7=s3^s4#补集
print(s7)
s8=s3-s4#差集
print(s8)

x=((1,2),(3,4))
for a,b in x:
    print(a,b)