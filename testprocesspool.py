# 进程池的同步调用
import os,time
from multiprocessing import Pool

def work(n):
    print('%s run' %os.getpid())
    time.sleep(2)
    return n**2

if __name__ == '__main__':
    p=Pool(3) #进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l=[]
    for i in range(10):
        res_l.append(p.apply(work,args=(i,)))
      # 同步调用，直到本次任务执行完毕拿到return，
      # 等待任务work执行的过程中可能有阻塞也可能没有阻塞
       # 但不管该任务是否存在阻塞，同步调用都会在原地等着
    print(res_l)