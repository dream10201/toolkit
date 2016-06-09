#!/bin/env python
# -*- coding:utf-8 -*-

## 修改文件指定位置一个字符，达到修改文件MD5的作用。
## 在2016年5月亲测百度云盘可以使用。
##
import sys

if __name__=='__main__':
    if len(sys.argv) <2:
        print 'Usage: %s < input file > [modify from position] [new char]'%(sys.argv[0])
        print "e.g. Replace the 2048th character to 'a' from the end of the file:"
        print "    python %s c:\\test.mkv -2048 a"%(sys.argv[0])
        sys.exit(0)
    fname =sys.argv[1]
    
    pos =-1023
    if len(sys.argv) >=3:
        pos =int(sys.argv[2])
        
    newChar ='x'
    if len(sys.argv) >=4:
        newChar =sys.argv[3]
    
    f =open(fname,'r+')
    
    # 0 is from begin, 2 is from reverse
    isReverse =0
    if pos<0:
        isReverse =2
    
    f.seek(pos, isReverse)
    old =f.read(1)
    print 'old=',old
    new =newChar[0:1]
    print 'new=',new
    f.seek(pos, isReverse)
    f.write(new)
    f.close()
