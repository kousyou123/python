# 查看主进程和子进程的进程号
import os
from multiprocessing import Process

def f(x):
    print('子进程id ：', os.getpid(), '父进程id ：', os.getppid())
    return 

if __name__ == '__main__':
    print('主进程id ：', os.getpid())
    for i in range(5):
        p = Process(target=f, args=(i,))
        p.start()