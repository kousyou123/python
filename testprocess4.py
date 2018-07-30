# 异步非阻塞
import os
import time
from multiprocessing import Process

def f(x):
    print('子进程id ：', os.getpid(), ' 进程 ：', x)
    time.sleep(1)

if __name__ == '__main__':
    print('主进程id ：', os.getpid())
    for i in range(5):
        p = Process(target=f, args=(i,))
        p.start()
    print(10*'*')