# join-异步阻塞，多个子进程同时运行，且所有子进程运行完后才执行主进程中join后面的代码
import os
import random
import time
from multiprocessing import Process

def f(i):
    print('子进程id ：', os.getpid())
    # 随机睡眠1-5秒
    time.sleep(random.randint(1, 5))
    print(' 进程 ：', i)

if __name__ == '__main__':
    print('主进程id ：', os.getpid())
    p_list = [ ]
    for i in range(5):
        p = Process(target=f, args=(i,))
        p.start()
        p_list.append(p)
    for l in p_list:
        print(l)
        l.join()
    print(10*'*')