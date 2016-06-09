#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import socket
import logging
from multiprocessing import Process
from threading import Thread
import tcploader_run

# default configurations.
conf ={ 'host':'im.studyfun.cn',
        'port':443,
        'process_count':1,
        'thread_count':1,
        'log_file':'./tcploader.log',
        'log_level':20
       }
            
def ParseConf(conffile):
    modname =conffile.rstrip('.py')
    (modpath,modname) =os.path.split(modname)
    sys.path.append(modpath)
    __import__(modname)
    attrs =dir(sys.modules[modname])
    for attr in attrs:
        if conf.has_key(attr):
            conf[attr] =getattr(sys.modules[modname], attr)
    
    
def ThreadRun(p,t,conf):
    tcploader_run.Run(p,t,conf)
    
def ProcessRun(p,conf):
    if conf['thread_count'] >1 :
        l = [ Thread(target = ThreadRun, args=(p,t,conf)) for t in xrange(0,conf['thread_count']) ]
        for i in l:
            i.start()
        for i in l:
            i.join()
    else :
        ThreadRun(p,0,conf)
    
if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print 'Usage: %s <configure file> \n'%(sys.argv[0])
        sys.exit()

    conffile =sys.argv[1]
    ParseConf(conffile)
    
    logging.basicConfig(level=conf['log_level'],
                    format='%(asctime)s %(levelname)s [p%(process)d t%(thread)d] [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=conf['log_file'],
                    filemode='a')
                
    logging.info('main started.')
    logging.debug('conf=%s',str(conf))
    
    if conf['process_count'] >1 :
        # 多进程
        l = [ Process(target = ProcessRun, args=(p,conf)) for p in xrange(0,conf['process_count']) ]
        for i in l:
            i.start()
        for i in l:
            i.join()
    else :
        ProcessRun(0,conf)

        
