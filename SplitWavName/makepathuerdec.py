from mkpathR import mksplittedpath
from mkpathR import copytodir
import os
import re
import shutil

#反回新的文件夹字典
def splitwavname(name):
    '''
    不用正则，时间基本一样：
    pathlist = name.split(" ")
    pathlist[1],pathlist[2]=pathlist[2],pathlist[1]
    pathlist.pop()
    '''
    pattern = r"(str\d) (\w+_\w+_\w+_\w+) (fret_\d+_\d+_\d+)"
    m=re.match(pattern,name)
    pathlist=[]
    if m:
        pathlist.append(m.group(1))
        pathlist.append(m.group(3))
        pathlist.append(m.group(2))
    else:
        print("can not match")
        raise
    return pathlist

#遍历文件夹获取（wav名字,old全路径）
def walkdir(dirname):
    dirlist=[]
    for path in os.walk(dirname):
        if len(path[2])>0:
            for i in path[2]:
                fullpath=os.path.join(path[0],i)
                dirlist.append((i,fullpath))
    #print(dirlist)
    return dirlist

#make path and get the newfilepath
@mksplittedpath
def addheadpath(headpath, pathlist):
    #print(os.path.join(headpath, pathlist[0], pathlist[1], pathlist[2]))
    return os.path.join(headpath, pathlist[0], pathlist[1], pathlist[2])

#copy...
def copyandmakepath(walkdirlist,newfolder):

    for itemtu in walkdirlist:
        pathlist=splitwavname(itemtu[0])
        #print(pathlist)
        shutil.copy(itemtu[1],os.path.join(addheadpath(newfolder,pathlist),itemtu[0]))


if __name__=="__main__":

    ne = r"D:\aaa"
    import time
    time1=time.time()
    copyandmakepath(walkdir(r"D:\samples_denoise_20170331\str5"),ne)
    diff = time.time() - time1
    print(diff)     #0.62s用两个装饰器
                            #0.36-0.42s使用一个装饰器，和不用的基本一样了。

