from random import random
from array import array

floats1=array('d', (random() for i in range(10**7)))
print(floats1[-1])

fp = open('floats.bin', 'wb')
floats1.tofile(fp) #把数组存入一个二进制文件里。
fp.close()
floats2 = array('d') #新建一个双精度浮点空数组。
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7) #把 1000 万个浮点数从二进制文件里读取出来。
fp.close()

print(floats2[-1])