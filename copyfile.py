# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:33:56 2018

@author: Inchel
"""

import os   

def mycopy(file1,file2):
    f1 = open(file1,'rb')
    f2 = open(file2,'wb')
    
    content = f1.readline()
    while len(content)>0:
        f2.write(content)
        content=f1.readline()
    f1.close()
    f2.close()
    
#自定义目录复制函数
def copydd(dir1,dir2):
    #获取被复制目录中的所有文件信息
    dlist = os.listdir(dir1)
    #创建新目录
    os.mkdir(dir2)
    #遍历所有文件，并执行文件复制
    for f in dlist:
        #为遍历的文件添加目录路径
        file1 = os.path.join(dir1,f)
        file2 = os.path.join(dir2,f)
        #判断是否是文件
        if os.path.isfile(file1):
            mycopy(file1,file2)
        
        if os.path.isdir(file1):
            copydd(file1,file2)#递归调用自己，来实现子目录的复制
            
def mycul(file):
    size = os.path.getsize(file)
    return size
        
def culdd(dir1):
    #获取被统计目录中的所有文件信息
    dlist = os.listdir(dir1)
    size = 0
    for f in dlist:
        file = os.path.join(dir1,f)
        if os.path.isfile(file):
            size += mycul(file)
        if os.path.isdir(file):
            size += culdd(file)
    return size
#测试
#copydd('./aa','./bb')
#print(culdd('./aa'))