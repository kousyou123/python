import datetime
import time


datenow=datetime.datetime.now()
time.sleep(2)
datenow1=datetime.datetime.now()
print(datenow)

print(datenow.__getattribute__("year"))

print(datenow.time())

print(datenow1-datenow)