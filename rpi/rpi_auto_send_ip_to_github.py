#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import time
import os
import sys
import urllib

add_parm_external =3  # 为公网IP中的4组数字各加一个值，用于隐藏真实的IP。 
add_parm_local =0  # 同上，用于内网IP。
if len(sys.argv)>1:
    add_parm_external =int(sys.argv[1])
if len(sys.argv)>2:
    add_parm_local =int(sys.argv[2])
print 'add_parm_external=',add_parm_external
print 'add_parm_local=',add_parm_local

def externalIp():
    url='http://1212.ip138.com/ic.asp'
    wp = urllib.urlopen(url) 
    content = wp.read()
    externalIpStr =content[content.index('[')+1: content.index(']')]
    return externalIpStr

s =None
external=''
local=''
preExternal=''
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.baidu.com', 80))
        external =externalIp()
        if external==preExternal:
            time.sleep(120)
            continue
        preExternal =external
        local =s.getsockname()[0]
    except Exception, e:
        print 'exc=',e
    else:
#        externalip =".".join( map(lambda x:str(int(x)+add_parm_external), external.split('.')) ) # same as the next line
        externalip =".".join([ str(int(x)+add_parm_external) for x in external.split('.') ])

#        localip =".".join( map(lambda x:str(int(x)+add_parm_local), local.split('.')) ) # same as the next line
        localip =".".join([ str(int(x)+add_parm_local) for x in local.split('.') ])

#        print 'externalip=',externalip
#        print 'localip=',localip

        now =time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))

        f=open('ip.txt','w+')
        f.write(now+"\n")
        f.write("external=\n")
        f.write(externalip+"\n")
        f.write("local=\n")
        f.write(localip+"\n")
        f.close()

        cmd ="git pull && git add ip.txt && git commit -a -m'update at %s' && git push -v"%(now)
        os.system(cmd)
    finally:
        s.close()
        time.sleep(900)



