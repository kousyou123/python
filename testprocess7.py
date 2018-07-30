# 继承Process类的形式开启进程
import os
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print('子进程：', os.getpid())
        print('%s 正在超进化' % self.name)

if __name__ == '__main__':

    p1 = MyProcess('暴龙兽')
    p2 = MyProcess('天使兽')
    p3 = MyProcess('加鲁鲁')

    # start方法会自动调用类中的run方法
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print('主进程：', os.getpid())