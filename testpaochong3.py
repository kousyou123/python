import requests
#from bs4 import BeautifulSoup
import time
import re
headers={    
    #'User-Agent':'Nokia6600/1.0 (3.42.1) SymbianOS/7.0s Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0'
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
info_lists=[]
def judgment_sex(class_name):
    if class_name=='womenIcon':
        return '女'
    else :
        return '男'
#f=open('C:/Users/Administrator/Desktop/lianxi/qiushi.text','a+')
def get_info(url):
    res=requests.get(url)
    #gbkTypeStr = res.text.encode("GBK", "ignore")
    #gbkTypeStr = res.text.encode("GB18030")
    #print(gbkTypeStr)
    #print(res.text)
    ids=re.findall('<h2>(.*?)</h2>',res.text,re.S)
    levels=re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
    sexs=re.findall('<div class="articleGender (.*?)">',res.text,re.S)
    contents=re.findall('<div class="content">.*?<span>(.*?)</span>',res.content.decode('utf-8'),re.S)
    laughs=re.findall('<i class="number">(\d+)</i>',res.text,re.S)
    comments=re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)
    #print(ids)
    #print(levels)
    #print(sexs)
    print(contents)
    #print(laughs)
    #print(comments)
    
    
    for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
        info={
            'id':id,
            'level':level,
            'sex':judgment_sex(sex),
            'content':content,
            'laugh':laugh,
            'comment':comment
        }
        #print("66666666666666666666666666666666666666666666666666666666666")
        
        info_lists.append(info)
        #print(info)



if __name__=='__main__':
    urls=['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,2)]
    for url in urls:
        get_info(url)
        time.sleep(2)
    for info_list in info_lists:
        #f=open('C:/Users/Administrator/Desktop/lianxi/qiushi.txt','a+')
        f=open('D:/qiushi.text','a+')
        try:
            f.write("姓名："+info_list['id']+'\n')
            f.write("等级："+info_list['level']+'\n')
            f.write("性别："+info_list['sex']+'\n')
            f.write(info_list['content']+'\n')
            f.write("点赞："+info_list['laugh']+'\n')
            f.write("评论数："+info_list['comment']+'\n\n')
            f.close()
        except UnicodeEncodeError:
            f.write("失败")