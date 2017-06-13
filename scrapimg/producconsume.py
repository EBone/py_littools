import Queue
import threading
import re
from  pyquery import PyQuery as pq
from papa import getImagurl
import time
from savfig import savimg

class Producer(threading.Thread):
    pattern = r"http://\w\w\d\.(.*)"
    match = re.compile(pattern)
    originurl = "http://jandan.net/ooxx"
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.queue=queue

    def getnextpage(self,url):

        sitecontent = pq(url)
        data = sitecontent('.cp-pagenavi')
        nexturl = pq(data(".previous-comment-page")).attr("href")[:-9]
        print nexturl
        self.queue.put(nexturl)
        time.sleep(1)
        self.getnextpage(nexturl)

    def run(self):
        self.getnextpage(self.originurl)

class Consumer(threading.Thread):
    def __init__(self,t_name,queue1,queue2,func):
        threading.Thread.__init__(self,name=t_name)
        self.queue1=queue1
        self.queue2=queue2
        self.func=func

    def run(self):
        while 1:
            url=self.queue1.get()
            urls=self.func(url)
            self.queue2.put(urls)
            time.sleep(1)

class Savefile(threading.Thread):
    namepattern = r"//\w\w\d\.\w+\.\w+/.+/(.*)"
    mm=re.compile(namepattern)

    def __init__(self,t_name,queue2,func):
        threading.Thread.__init__(self,name=t_name)
        self.queue2=queue2
        self.func=func
    def run(self):
        while 1:
            imglist=self.queue2.get()
            if imglist:
                for i in imglist:

                    gg=self.mm.match(i).groups()[0]
                    i = 'http:' + i
					
                    print gg
                    self.func(i,gg)
                    time.sleep(2)




if __name__=="__main__":
    import sys

    temp = sys.stdout
    sys.stdout = open('.server_all', 'w')

     # resotre print

    q1=Queue.Queue()
    q2=Queue.Queue()
    p=Producer('prourl',q1)
    c=Consumer('geturl',q1,q2,getImagurl)
    s=Savefile('savfig',q2,savimg)
    p.start()
    c.start()
    s.start()
    p.join()
    c.join()
    s.join()
    #sys.stdout.close()

