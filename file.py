import os
p="E:\\办公资料\\python\\pythontest\\test.txt"
p1="E:\办公资料\python\pythontest\\test1.txt"
p2="D:\Log\\b.txt"
#打开文件逐行读取 先转成二进制
data=open(p,'rb')
s = data.readlines()
data.close()
#循环处理每一行
for lines in s:
    decodedLine = lines.decode('utf8')
    print(decodedLine.replace("\n",""))
writedata=open(p,'a',encoding= 'utf8')#a 模式 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
writedata.write("adf啊都是废话\n") #将这句话写入文件
writedata.close()
#打开文件逐行读取 指定编码读取方式
writedata=open(p,'r',encoding= 'utf8')
s = writedata.readlines()
writedata.close()
#循环处理每一行
for lines in s:
    lines= lines.replace("\n","")#去掉空行
    print(lines)

writedata1=open(p1,'w',encoding='utf8')#w 模式 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
writedata1.write("adf啊都是废话\n") #将这句话写入文件
writedata1.close()
#打开文件逐行读取 指定编码读取方式
writedata1=open(p1,'r',encoding='utf8')
s = writedata1.readlines()
writedata1.close()
#循环处理每一行
for lines in s:
    print(lines)


