import time
import random
from multiprocessing import Process, Event

def car(i,e):  # 感知状态的变化
    if not e.is_set():    # 当前这个事件的状态如果是False
        print('car%s正在等待'%i)  # 这辆车正在等待通过路口
    e.wait()    # 阻塞 直到有一个e.set行为  # 等红灯
    print('car%s通过路口'%i)

def traffic_light(e):  # 修改事件的状态
    print('\033[1;31m红灯亮\033[0m')
    # 事件在创立之初的状态是False，相当于程序中的红灯
    time.sleep(2)  # 红灯亮2s
    while True:
        if not e.is_set():  # False
            print('\033[1;32m绿灯亮\033[0m')
            e.set()
        elif e.is_set():
            print('\033[1;31m红灯亮\033[0m')
            e.clear()
        time.sleep(2)

if __name__ == '__main__':
    e = Event()
    Process(target=traffic_light, args=[e, ]).start()
    for i in range(10):
        time.sleep(random.randrange(0, 5, 2))
        Process(target=car, args=[i, e]).start()