#利用装饰器

import os
import shutil
import functools

#装饰器一：拷贝前确认文件路径，没有则创建
def mksplittedpath(func):
    @functools.wraps(func)
    def wrapper(headpath,pathlist):
        #pathlist.pop()
        dirpath=''
        for path in pathlist:
            dirpath=os.path.join(dirpath,path)
            fulldirpath=os.path.join(headpath,dirpath)
            if not os.path.exists(fulldirpath):
                os.mkdir(fulldirpath)
        return func(headpath,pathlist)
    return wrapper

#装饰器二：用来给入src和des，为shutil.copy准备:可不用，效率不高
def copytodir(oldpath,pathname):
    def addheadwrap(func):
        @functools.wraps(func)
        def wrapper(headpath,pathlist):
            shutil.copy(oldpath,os.path.join(func(headpath,pathlist),pathname))
        return wrapper
    return addheadwrap




if __name__=="__main__":
    # 文件名字，可以通过os.walk获得，这里直接给出
    pathname = "str6 mut_solo_same_slow fret_000_000_000 rr_0.wav"
    pathlist = pathname.split(" ")
    # pathlist[1],pathlist[2]=pathlist[2],pathlist[1]
    # print(pathlist)
    # 被包装函数体返回新的路径
    @copytodir("D:\PythonProjects\py_littools\SplitWavName\str6 mut_solo_same_slow fret_000_000_000 rr_0.wav", pathname)
    @mksplittedpath
    def addheadpath(headpath, pathlist):
        return os.path.join(headpath, pathlist[0], pathlist[1], pathlist[2])

    addheadpath("D:\PythonProjects\py_littools\SplitWavName",pathlist)
    print(addheadpath.__name__)
