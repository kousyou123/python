# 计算出一个字符串的MD5值：
import hashlib
md5 = hashlib.md5()
md5.update(b'how to use md5 in python hashlib?') #注，要转换成b字节模式才能正常
print(md5.hexdigest()) # d26a53750bc40b38b65a520292f69306

# 如果数据量很大，可以分块多次调用update()，
# 一段字符串直接进行摘要和分成几段摘要的结果是相同的：

md5 = hashlib.md5()
md5.update(b'how to use md5 in ')
md5.update(b'python hashlib?')
print(md5.hexdigest()) # d26a53750bc40b38b65a520292f69306

#　md5摘要加密传输进来的明文密码
def md5_digest(user, plain_pass):
    md5 = hashlib.md5(user[::-1].encode('utf-8')) # 创建了一个md5算法的对象,且对定义的盐切片倒序
    md5.update(plain_pass.encode('utf-8'))
    return md5.hexdigest()

user = 'bilibili'
pwd = '123456'
print(md5_digest(user, pwd))  # b442d27216d7e1dd54d6419a9d31056f