# 进程池的异步调用
import os
import time
import random
from multiprocessing import Pool

def work(n):
    print('%s run' %os.getpid())
    time.sleep(random.random())
    return n**2

if __name__ == '__main__':
    p=Pool(3) #进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l=[]
    for i in range(10):
        res = p.apply_async(work, args=(i,))
        # 异步运行，根据进程池中有的进程数，每次最多3个子进程在异步执行
        # 返回结果之后，将结果放入列表，归还进程，之后再执行新的任务
        # 需要注意的是，进程池中的三个进程不会同时开启或者同时结束
        # 而是执行完一个就释放一个进程，这个进程就去接收新的任务。
        res_l.append(res)

    # 异步apply_async用法：如果使用异步提交的任务，主进程需要使用jion，
    # 等待进程池内任务都处理完，然后可以用get收集结果
    # 否则，主进程结束，进程池可能还没来得及执行，也就跟着一起结束了
    p.close()
    p.join()
    for res in res_l:
        print(res.get())
    # 使用get来获取apply_aync的结果,如果是apply,则没有get方法,
    # 因为apply是同步执行,立刻获取结果,也根本无需get。