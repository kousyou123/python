# join-同步阻塞，完全按顺序且运行完一个子进程后再到下一个
import os
import time
from multiprocessing import Process

def f(i):
    print('子进程id ：', os.getpid(), ' 进程 ：', i)
    time.sleep(1)

if __name__ == '__main__':
    print('主进程id ：', os.getpid())
    for i in range(5):
        p = Process(target=f, args=(i,))
        p.start()
        p.join()  # 在运行多进程的for里面加join，就从异步非阻塞变成了同步阻塞了
    print(10*'*')