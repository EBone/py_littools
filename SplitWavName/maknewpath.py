import re
import os.path
import os
import shutil

'''
tstr="str4 mut_solo_first_slow fret_001_001_001 rr_2.wav"
#pattern=r"(str\d) (\w+_\w+_\w+_\w+) (fret_\d+_\d+_\d+)"
#print(re.match(pattern,tstr).groups())
'''

#反回新的文件夹字典
def splitwavname(name):
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

    #print(pathlist)
    return pathlist

#新的非全路径
def makesecondpartpath(pathlist):
    partpath=os.path.join(pathlist[0],pathlist[1],pathlist[2])
    #print(partpath)
    return partpath

def makefirstpartpath(pathlist):
    partpath = os.path.join(pathlist[0], pathlist[1])
    #print(partpath)
    return partpath

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


def copyandmakepath(walkdirlist,newfolder):
    for itemtu in walkdirlist:
        pathlist=splitwavname(itemtu[0])
        firstpartpath=makefirstpartpath(pathlist)
        secondpartpath=makesecondpartpath(pathlist)
        #print(newfolder)
        firstfullpath=os.path.join(newfolder,firstpartpath)
        secondfullpath=os.path.join(newfolder,secondpartpath)

        #创建str下的两级目录
        if not os.path.exists(firstfullpath):
            os.mkdir(firstfullpath)
        if not os.path.exists(secondfullpath):
                os.mkdir(secondfullpath)
        newfullname=os.path.join(secondfullpath,itemtu[0])

        #copy。。。
        shutil.copy(itemtu[1],newfullname)

#创建 str4-7的目录
def makestrpath(newfolder):
    stringlist=['str4','str5','str6','str7']
    for i in stringlist:
        newstrpath=os.path.join(newfolder,i)
        if not os.path.exists(newstrpath):
            os.mkdir(os.path.join(newfolder,i))



if __name__=="__main__":
    #print(os.getcwd())
    #makepartpath(splitwavname(tstr))
    #walkdir(r"D:\samples_denoise_20170331\str4")
    #ne是要转移到的顶级目录
    import time
    ne=r"D:\aaa"
    makestrpath(ne)
    time1=time.time()
    copyandmakepath(walkdir(r"D:\samples_denoise_20170331\str5"), ne)
    #copyandmakepath(walkdir(r"D:\samples_denoise_20170331\str5"),ne)
    #copyandmakepath(walkdir(r"D:\samples_denoise_20170331\str6"), ne)
    #copyandmakepath(walkdir(r"D:\samples_denoise_20170331\str7"), ne)
    diff=time.time()-time1
    print(diff)     #0.37s
