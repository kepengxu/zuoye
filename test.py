# -*- coding: utf-8 -*-
#!/usr/bin/python

import os,shutil

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print "move %s -> %s"%( srcfile,dstfile)

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print "copy %s -> %s"%( srcfile,dstfile)


if __name__=='__main__':
    source='/home/cooper/Dataset/results'
    target='/home/cooper/Dataset/resultstarget'
    l=os.listdir(source)
    for name in l:
        sourcepath=os.path.join(source,name)


        #print sourcepath,targetpath
        p1=filter(str.isalpha, name)
        p2=filter(str.isdigit,name)
        p=p1[:-3]
        if p=='deeplabv':
            p2=p2[1:]
            p=p+'3plus'
        print p,p2
        after=p2+'_'+p+'.jpg'
        targetpath = os.path.join(target,after)
        mycopyfile(sourcepath,targetpath)
