import threading, time

# 将躲迷藏中搜寻的角色这个类创造出来,且继承了线程Thread这个类
class Seeker(threading.Thread):

    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        # 睡一秒，让躲猫猫的面码也运行起来，不然会阻塞住
        time.sleep(1)
        self.cond.acquire()
        print(self.name + ': (藏)好了吗？')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': (藏)好了吗？~~')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 看到你了！面码！')
        self.cond.notify()
        self.cond.wait()
        self.cond.release()
        print(self.name + ": 谢谢你，面码~ ")

# 再来是躲迷藏的面码
class Hider(threading.Thread):

    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        # 释放对锁的占用，同时线程挂起来在这里，直到被notify
        print(self.name + ": 还没好哦~")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": (藏)好了哦~")
        self.cond.notify()
        self.cond.wait()
        self.cond.notify()
        self.cond.release()
        print(self.name + ": 阿，被看到了~")
if __name__ == '__main__':
    cond = threading.Condition()
    seeker = Seeker(cond, "仁太")
    hider = Hider(cond, "面码")
    seeker.start()
    hider.start()