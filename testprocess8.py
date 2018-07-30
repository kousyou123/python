import time
import sys
import random
from multiprocessing import Process

class MyProcess(Process):

    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('[%s] 超进化' % self.name)
        time.sleep(random.randint(1, 5))
        self.viewBar(100)
        print('[%s] 进化完毕！')

    def viewBar(self, i):
        """
        进度条效果
        """
        for count in range(0, i + 1):
            second = 0.1
            time.sleep(second)
            sys.stdout.write('\r 超进化 >>>:%.0f%%' % count)
        sys.stdout.flush()

if __name__ == '__main__':

    p1 = MyProcess('亚古兽')
    p1.start()
    # 睡眠10秒以便展现run中的方法，当然主进程睡眠10秒仍未能执行完子进程的
    time.sleep(10)

    # 关闭进程，但不会立即关闭，所以使用is_alive立刻查看的结果可能还是存活
    p1.terminate()
    print('\n 进程存活:', p1.is_alive())

    print('进化失败')
    time.sleep(0.1)
    print('进程存活:', p1.is_alive())