tu=(1,2,3)
tu1=([1,2,3],["a","b"])
print("".join([str(x) for x in tu]))#字符串拼接
print("".join([str(x) for x in tu1]))#字符串拼接

string="I {} Python! {}".format("Love","hello world!")#可以不指定下标
print(string)
string="I {0} Python! {1} {0} {1}".format("Love","hello world!")#可以重复多次指定下标
print(string)
string="I {para} Python! {para1} {para1}".format(para="Love",para1="hello world!")#可以为下标指定名称
print(string)

string1=string.replace(" ","*")#返回的为新的字符串
print(string)#原来的字符串不变
print(string1)#新的字符串结果改变了