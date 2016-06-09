#!/bin/evn python
#-*- encoding: utf-8 -*-

import os
import time
import random

# 15秒(time_check)检测一次，检测最近3分钟(timve_interval)内有多少张图片，
#   (从上次发送的照片下一张算起)超过30张(send_watermark)时就平均发送10张(send_count)。发送之后保存最后一张照片名称。
#   发送完之后休息15分钟(time_sleep_after_sent)。

time_check=15
timve_interval=180
send_watermark=30
send_count=10
time_sleep_after_sent=900
path='/tmp/motion/'


last_sent_file_create_time =0

def TrySend(files):
    global last_sent_file_create_time
    for x in files:
        created_time =os.path.getctime(x)
        if created_time>last_sent_file_create_time:
            last_sent_file_create_time =created_time
    print 'last_sent_file_create_time=',last_sent_file_create_time

    time.sleep(time_sleep_after_sent)
    pass

def Run():
    global last_sent_file_create_time
    while True:
        time.sleep(time_check)

        fl = os.listdir(path)

        time_now =time.time()
        sendlst =[]
        for x in fl:
            if os.path.splitext(x)[1]!=".jpg":
                continue
            filename =path+x
            created_time =os.path.getctime(filename)
            #print 'filename=',filename
            #print 'created_time=',created_time
            if time_now-created_time<timve_interval:
                sendlst.append(filename)
            
        print 'sendlst=',sendlst
        if len(sendlst)<send_watermark:
            continue

        reslst =[]
        for x in sendlst:
            created_time =os.path.getctime(x)
            if created_time>last_sent_file_create_time:
                reslst.append(x)
        print 'reslst=',reslst
        if len(reslst)<send_watermark:
            continue

        rt = random.sample(reslst, send_count)  #从list中随机获取n个元素，作为一个片断返回 
        print '#### rt=',rt
        TrySend(rt) 

#        break ####


if __name__ == '__main__':
    while True:
        try:
            Run()
#            break ####
        except Exception, e:
            print e
            continue
