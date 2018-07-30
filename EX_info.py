#coding:utf-8 
from bs4 import BeautifulSoup
import bs4
import os
import time
import csv
import codecs

#读取XML内的文件数据并存入CSV格式的文件--可使用EXCEL打开
def open_file():
    file_folder= 'C:\\Users\\Administrator\\Desktop\\File\\Filename' ##文件夹位置
    if os.path.isdir(file_folder):
        for fileName in os.listdir(file_folder):
           # print fileName
            info(fileName) ##读取文件名字
def info(fileName):
    soup = bs4.BeautifulSoup(open('C:/Users/Administrator/Desktop/File/Filename/'+fileName))
    a = soup.find_all('mxxx')
    info = []
    for i in a:
        dt=[]
        dt.append(i.find('fpdm').get_text().strip())
        dt.append( i.find('fphm').get_text().strip())
        dt.append(i.find('kprq').get_text().strip())
        dt.append(i.find('gmfnsrsbh').get_text().strip()+'\n')
        dt.append( i.find('je').get_text().strip())
        dt.append(i.find('se').get_text().strip())
        dt.append(float( i.find('je').get_text().strip())  + float(i.find('se').get_text().strip()))
        info.append(dt)
    with open("Ex_info.csv","ab+") as csvfile: ##“ ab+ ”去除空白行，又叫换行！
        csvfile.write(codecs.BOM_UTF8)  ##存入表内的文字格式
        writer = csv.writer(csvfile)  #存入表时所使用的格式
        writer.writerow(['发票代码','发票号码','时间','纳税人识别号','未税金额','税额','总金额'])
        writer.writerows(info) #写入表
    
if __name__ == '__main__':
    open_file()
