# join方法能够检测到子进程是否已经执行完了，阻塞直到子进程执行结束。
import time
from multiprocessing import Process

def func(name):
    print('hello', name)
    time.sleep(3)
    print('我是子进程')

if __name__ == '__main__':
    # 实例化一个子进程，执行func函数，传输参数
    p = Process(target=func, args=('tiele',))
    # 运行子进程对象
    p.start()
    # 主线程等待p终止
    p.join()
    print('我是父进程')