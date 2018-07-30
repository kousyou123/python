import time
from multiprocessing import Process

def func(name):
    print('hello', name)
    print('我是子进程')

if __name__ == '__main__':
    # 实例化一个子进程，执行func函数，传输参数
    p = Process(target=func, args=('tiele',))
    #　运行子进程对象
    p.start()
    time.sleep(1)
    print('执行主进程的内容了')