import numpy #安装 NumPy 之后， 导入它（NumPy 并不是 Python 标准库的一部分） 。

a=numpy.arange(12) #新建一个 0~11 的整数的 numpy.ndarry， 然后把它打印出来。
print(a)
print(a.shape) #看看数组的维度， 它是一个一维的、 有 12 个元素的数组。
a.shape=3,4 #把数组变成二维的， 然后把它打印出来看看。
print(a)
print(a[2]) #打印出第 2 行。
print(a[2,1])#打印第 2 行第 1 列的元素。
print(a[:, 1])#把第 1 列打印出来。
print(a.transpose())#把行和列交换， 就得到了一个新数组

