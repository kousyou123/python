array=[9,8,7,4,6,2]
array1=[2]
array.sort()
array.insert(0,1)
print(array)
print(array+array1)
a=[1,2,3,4,5]
b=[9,8,7,6,5]
d=[]
for x in zip(a,b):#将元素打包成一个个元组
    d.append(x)
print(d)
c=[(1,2),(3,4)]
for y in zip(*c):#将元素解压为列表
    print(y)
weeks =["sun","mon","tue","web","tue","fri","sta"]
for k,v in enumerate(weeks,1):#可传入开始下标
    print(k,v)

