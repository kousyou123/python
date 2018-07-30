import time
def dec(func):
    def inner():
        print("running inner")
    return inner # dec 返回 inner 函数对象。

@dec
def targetoutter(): #使用 dec 装饰 targetoutter
    print("running targetoutter")


print(targetoutter()) #调用被装饰的 targetoutter 其实会运行 inner

print(targetoutter) #审查对象， 发现 targetoutter 现在是 inner 的引用

def counttime(func):
    def timespan(*args):
        t0=time.time()
        result=func(*args)
        t1=time.time()-t0
        print(t1)
        return result
    return timespan

@counttime
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(6))