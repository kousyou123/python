import socket

client = socket.socket()
ip = input('输入服务端ip:')
port = input('输入端口:')
# 通过ip和端口连接服务端
client.connect((ip, int(port)))
print('这里是客户端')
while 1:
    res = input('>>>').strip()
    # 客户端传送消息给服务端
    client.send(res.encode('utf-8'))
    if res.upper() == 'Q':
        break
    # 客户端接收服务端传过来的消息
    ret = client.recv(1024)
    if ret.upper() == 'Q':
        break
    print(ret.decode('utf-8'))
client.close()