array1=[1,3,5,7,9]
array2=[3,6,9]
array=[]

for i in range(0,101,2):
    array.append(i)
print(array[::-2])
arraynew=[x for x in array1 if x in array2]#列表推导 简单实用 上传测试
print(arraynew)
arraysort=[9,7,1,2,5,3]
#冒泡排序
for j in range(len(arraysort)-1):
    for k in range(len(arraysort)-1-j):
       if arraysort[k]>arraysort[k+1]:
           arraysort[k],arraysort[k+1]=arraysort[k+1],arraysort[k] 
   
print(arraysort)
        