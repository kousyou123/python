import itchat, time
from itchat.content import *
headImgPath="D:\IMAGE\\"
itchat.auto_login()
for friend in itchat.get_friends(update=True)[0:]:
    #可以用此句print查看好友的微信名、备注名
    print(friend['NickName']+"("+friend['RemarkName']+")")
    img = itchat.get_head_img(userName=friend["UserName"])
    path = headImgPath+friend['NickName']+"("+friend['RemarkName']+").jpg"
    try:
        with open(path,'wb') as f:
            f.write(img)
    except Exception as e:
        print(repr(e))