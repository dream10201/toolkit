#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys


# inputDir/
# ----inputFilePrefix_0
# ----inputFilePrefix_1
# ----inputFilePrefix_2
# 
# outputDir

def MergeFile(inputDir, inputFilePrefix, outputDir):
    if not os.path.exists(inputDir):
        return False

    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    partno = 0
    outFile = open(outputDir+'/'+inputFilePrefix,'wb')
    while True:
        fname = os.path.join(inputDir,inputFilePrefix + '_' + str(partno))
        if not os.path.exists(fname):
            return False
        print 'read start %s' % fname
        inFile = open(fname,'rb')

        fileSize =os.path.getsize(fname)
        left =fileSize
        while left>0:
            toRead =16*1024*1024 # 每次读写的大小.
            if left < toRead:
                toRead =left
            content = inFile.read(toRead)
            n =len(content)
            if n>0:
                left -=n
                outFile.write(content)
            else : 
                break

        partno += 1
    outFile.close()

if __name__ == '__main__':
    if len(sys.argv)<4:
        print 'Usage: %s inputDir, inputFilePrefix, outputDir.'%(sys.argv[0])
        print '    e.g.  %s ./split_dir,./input_file,./merge_dir'%(sys.argv[0])
        sys.exit()

    MergeFile(sys.argv[1], sys.argv[2], sys.argv[3])

