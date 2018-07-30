import socket
from socket import SOL_SOCKET, SO_REUSEADDR

'''
实例化一个socket模块中的socket类的对象，为便于区别，在服务端我起名server
可比喻为买手机
'''
server = socket.socket()

'''
此socket配置要在bind之前，用处是表示重用ip和端口,
防止上次异常退出后再启动报地址在使用或端口被占用之类的错误
可比喻为实名认证后下面的手机号码就属于你的了
'''
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

'''
表示服务端捆绑的ip地址与端口，在这里为本机测试故填回环地址127.0.0.1,
端口是int类型的可用端口范围内的数字,
可比喻为买手机卡.
'''
server.bind(('127.0.0.1', 9527))

# 表示开启侦听
server.listen() #　可比喻为手机开机，能接收到信号了

# 同意接收客户端链接，并将客户端的链接信息赋给两个变量
conn, addr = server.accept()

# 好奇的话可以print打印看看分别是什么
print(conn)
'''
拿到的是类似这样的，链接过来的客户端信息:
<socket.socket fd=300, family=AddressFamily.AF_INET, 
type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9527), 
raddr=('127.0.0.1', 61463)>
'''

print(addr)
# 拿到的是一个元组,里面包含有客户端ip和端口('127.0.0.1', 61463)
# 做成循环模式，以便不断交互对话
print('这里是服务端')

while 1:
    # 接收客户端发送过来的字节信息
    ret = conn.recv(1024)

    # 如果客户端发送q/Q过来，表示退出聊天
    if ret.upper == 'Q': break

    # 打印并解码显示出来
    print(ret.decode('utf-8'))

    # 服务端这边也做成可以输入反馈开始尬聊，一人一句
    res = input('>>>').strip()

    # send方法代表发送消息过去客户端，需要转码
    conn.send(res.encode('utf-8'))

    # 自己这方也可以发送中止信号
    if res.upper() == 'Q':break

conn.close()
server.close()