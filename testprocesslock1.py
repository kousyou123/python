#加锁同步控制
# 只要用到了锁，锁之内的代码就变成同步的了。
# 锁 ：控制一段代码，同一时间，只能被一个进程执行。

import time
import random
from multiprocessing import Process, Lock

def work(lock, person, n):
    # 加锁由并发变成了串行，牺牲了运行效率，但避免了对资源的竞争
    lock.acquire()
    print('%s 开始闯黄道十二宫中的 [第%s宫] 了！' % (person, n))
    time.sleep(random.random())
    print('%s 闯过了 [第%s宫]！' % (person, n))
    # lock中的方法，acquire和release可说是一对组合，先加锁再解锁并将锁重置
    lock.release()

if __name__ == '__main__':
    # Lock得先创造一个实例出来，才方便使用它当中的方法
    lock = Lock()
    start = ['星矢', '一辉', '冰河', '紫龙', '阿瞬']
    for i in range(1, 13):
        role = random.choice(start)
        p = Process(target=work, args=(lock, role, i))
        p.start()