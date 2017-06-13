import urllib2
#import re
#namepattern=r'http://\w+\.\w+\.\w+/.*/(.*)'
import socket

import os.path
def savimg(url,fname):
    print url
    try:
        request=urllib2.urlopen(url)
        with open(os.path.join(r'D:\ooxx0609',fname),'wb') as g:
            g.write(request.read())
            request.close()
    except urllib2.HTTPError,e:
        print "caocaocao"
    except socket.timeout,f:
        print "__timeout__"
'''
f=urllib2.urlopen('http://ww1.sinaimg.cn/thumb180/707c5757gw1f9shjpofvrg20b4068b29.gif')
pic=f.read()
with open("1.gif",'wb') as g:
    g.write(pic)
'''

if __name__=="__main__":
	import sys
	savimg(sys.argv[1],sys.argv[1].split('/')[-1])
	
	