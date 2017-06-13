from  pyquery import PyQuery as pq
import re
pattern=r"//\w\w\d\.(.*)"
match=re.compile(pattern)
originurl="http://jandan.net/ooxx/page-80"

def getImagurl(url):
    urls=[]
    sitecontent=pq(url)
    data=sitecontent('img')
    print(data)
    for i in data:
        imageurl=pq(pq(i).siblings('a')).attr('href')
        if isinstance(imageurl,str) and match.match(imageurl):
            urls.append(imageurl)

    print urls
    return urls

n=0
pages=[]
def getnextpage(url):
    global n
    if n==10:
        return
    sitecontent=pq(url)
    data=sitecontent('.cp-pagenavi')
    nexturl=pq(data(".previous-comment-page")).attr("href")
    print nexturl
    pages.append(nexturl)
    n=n+1
    getnextpage(nexturl)

i=0
'''
def savefile(file):

    global i
    filedir=r"D:/"
    name=str(i)+".jpg"
    with open(filedir+name,'w') as g:

'''
if __name__=="__main__":
    getnextpage(originurl)
    print pages

    for i in pages:
        getImagurl(i)


