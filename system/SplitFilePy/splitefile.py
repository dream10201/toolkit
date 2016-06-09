#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys

def SplitFile(inputFile, outputDir, partSize):
    if not os.path.isfile(inputFile):
        return False
    inputSize =os.path.getsize(inputFile)

    filedir,name = os.path.split(inputFile)
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    totalLeftSize = inputSize
    partno = 0
    inFile = open(inputFile,'rb')
    while totalLeftSize>0:
        fname = os.path.join(outputDir,name + '_' + str(partno))
        print 'write start %s' % fname
        outFile = open(fname,'wb')

        readSize = 0
        while readSize < partSize:
            left =partSize-readSize
            if totalLeftSize < left:
                left =totalLeftSize

            toRead =16*1024*1024 # 每次读写的大小.
            if left < toRead:
                toRead =left
            content = inFile.read(toRead)
            n =len(content)
            if n>0:
                readSize += n
                totalLeftSize -=n
                outFile.write(content)
            else : 
                break
         
        outFile.close()
        if totalLeftSize==0 :
            break
        partno += 1
    inFile.close()

if __name__ == '__main__':
    if len(sys.argv)<4:
        print 'Usage: %s inputFile, outputDir, partSize.'%(sys.argv[0])
        print '    e.g.  %s ./input_file,./split_dir,4*1024*1024'%(sys.argv[0])
        sys.exit()

    SplitFile(sys.argv[1],sys.argv[2],eval(sys.argv[3]))

