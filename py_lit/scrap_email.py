import requests
from pyquery import PyQuery as pq

class Collect_Email:
    def __init__(self,url):
        self.rooturl="http://forums.threebodytech.com/"
        self.response=None
        self.url=url
        self.namelist=[]
        self.pages=[]
    def login(self,redirect):
        payload={'username':'admin','password':'m_idi2audiO_603','redirect':redirect,'sid':'17d03b96951dee64adb75580f6153078','login':'Login'}
        r=requests.post('http://forums.threebodytech.com./ucp.php?mode=login',data=payload)
        print(r.status_code)
        return r
    def get_url_content(self,url):
        r=requests.get(url)
        self.response=r.content.decode('utf-8')

    def get_user_content(self):
        doc=pq(self.response)('strong .username')
        for i in doc.items():
            taddr=i.attr('href')
            tnum=taddr.find(("&sid"))
            addr=taddr[:tnum]
            self.namelist.append([i.text(),addr])

    def get_email_address(self):
        mailist=[]
        for item in self.namelist:
            result=self.login(item[1])
            content=result.content.decode("utf-8")
            doc=pq(content)(".column1 dl dd a").attr("href")
            print(doc)
            tnum=doc.find(":")
            item[1]=doc[tnum+1:]
        print(self.namelist)


    def get_next_pages(self):
        doc=pq(self.response)(".next").siblings()
        page_set=set([])
        temp=[]
        for i in doc.items():
            temp_addr=i("a").attr("href")
            if temp_addr:
                temp.append(self.rooturl+temp_addr)
            page_set.update(temp)
        return page_set

    def get_all(self):
        self.get_url_content(self.url)
        self.get_user_content()
        for url in self.get_next_pages():
            self.get_url_content(url)
            self.get_user_content()

        self.get_email_address()

if __name__=="__main__":
    url="http://forums.threebodytech.com/viewtopic.php?f=12&t=63"
    p=Collect_Email(url)
    p.get_all()
    #p.login()
    #p.get_user_content()
    #addr=p.get_email_address()
    #print(addr)
    # f=open("test.html",'wb')
    # f.write(addr[0])
    # f.close()
    # f = open("test2.html", 'wb')
    # f.write(addr[1])
    # f.close()
    # f = open("test2.html", 'wb')
    # f.write(addr[1])
    # f.close()
