# import threading
#
# def p():
#     print ('timer is on.')
#     t = threading.Timer(2,p)
#     t.start()
#
# if __name__ == '__main__':
#     p()
from datetime import datetime , timedelta
from time import sleep
import itchat
import os , random

SECONDS_PER_DAY = 24 * 60 * 60

#@a8832fb546928398be13a510be8ac84e     松下拙石
#@fdc7a51de70bada5196354bd21feb03cdcc48dd4fab91c6fa8c631f1766ce319     CharlieChen

def getapic():
    rootdir=r'd:\Github\ToShen\pics'
    list=os.listdir(rootdir)
    return os.path.join(rootdir , random.choice(list))

def doFunc(sendpic):
    print ('Now sending %s...'%sendpic)
    itchat.send('@img@%s' %sendpic , toUserName='@fdc7a51de70bada5196354bd21feb03cdcc48dd4fab91c6fa8c631f1766ce319')

'''
itchat.send('@img@%s' % 'gz.gif')
itchat.send('@fil@%s' % 'xlsx.xlsx')
itchat.send('@vid@%s' % 'demo.mp4')
'''

def doFirst():
    curTime = datetime.now()
    print (curTime)
    desTime = curTime.replace(hour=17, minute=49, second=0, microsecond=0)
    if desTime<curTime:
        desTime=desTime + timedelta(days=1)
    print (desTime)
    delta = desTime - curTime
    print (delta)
    skipSeconds = delta.total_seconds()
    print ("Next time for task must sleep %d seconds" % skipSeconds)
    sendpic=getapic()
    print ('now setting a task to send the %s ...' %sendpic)
    sleep(skipSeconds)
    doFunc(sendpic)

def login_wechat():
    itchat.login()
    itchat.send(u'现在开始定时发送微信的任务', 'filehelper')
    # friends = itchat.get_friends(update=True)[0:]
    # male = female = other = 0 # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算 # 1表示男性，2女性
    # for i in friends[1:]:
    #     sex = i["Sex"]
    #     if sex == 1:
    #         male += 1
    #     elif sex == 2:
    #         female += 1
    #     else:
    #         other += 1 # 总数算上，好计算比例啊～
    # total = len(friends[1:]) # 好了，打印结果
    # print (u"男性好友：%.2f%%" % (float(male) / total * 100))
    # print (u"女性好友：%.2f%%" % (float(female) / total * 100))
    # print (u"其他：%.2f%%" % (float(other) / total * 100))
    # sig , prov = []
    # for i in friends[1:]:
    #     sig.append(i['Signature'])

if __name__ == "__main__":
    login_wechat()
    #2.Start the Timer:1)get a file 2)doFirst()
    doFirst()

