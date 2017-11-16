import requests
from pyquery import PyQuery as pq
import time
class Collect_Email:
    def __init__(self,url):
        self.rooturl="http://forums.threebodytech.com/"
        self.response=None
        self.url=url
        self.namelist=[]
        self.session=requests.session()

    def login(self):
        payload={'username':'admin','password':'m_idi2audiO_603','redirect':'./ucp.php?mode=login','sid':'7badcbe3d8df44a66ce44dc8d30380c8','login':'Login'}
        self.session.post('http://forums.threebodytech.com/ucp.php?mode=login',data=payload)

    #还是先登陆吧
    def get_url_content(self,url):
        r=self.session.get(url)
        self.response=r.content.decode('utf-8')

    #每页的用户网址
    def get_user_content(self):
        doc=pq(self.response)('strong .username')
        for i in doc.items():
            taddr=i.attr('href')
            #print(taddr)
            if "&sid" in taddr:
                tnum=taddr.find("&sid")
                addr=taddr[:tnum]
            else:
                addr=taddr
            #print(addr)
            name_addr=[i.text(),self.rooturl+addr]
            if name_addr not in self.namelist:
                self.namelist.append(name_addr)

    #全部email_address
    def get_email_address(self):
        mailist=[]
        for item in self.namelist:
            time.sleep(1)
            self.get_url_content(item[1])
            doc=pq(self.response)(".column1 dl dd a").attr("href")
            print(doc)
            if doc:
                tnum=doc.find(":")
                item[1]=doc[tnum+1:]
            else:
                print("fuck")
                print(self.response)
        print(self.namelist)

    #下一页地址(可优)
    def get_next_pages(self):
        doc=pq(self.response)(".next").siblings()
        page_list=[]
        temp=[]
        for i in doc.items():
            temp_addr=i("a").attr("href")
            if temp_addr:
                temp.append(self.rooturl+temp_addr)
        for addr in temp:
            if addr not in page_list:
                page_list.append(addr)
        print(len(page_list))
        return page_list

    #此处调用
    def get_all(self):
        self.login()
        self.get_url_content(self.url)
        self.get_user_content()
        for url in self.get_next_pages():
            self.get_url_content(url)
            self.get_user_content()
        self.get_email_address()
        self.session.close()


def make_name_mail(name_list):
    name_str_items=[]
    for item in name_list:
        str_item='              '.join(item)
        name_str_items.append(str_item)
    return name_str_items

def make_mail(name_list):
    mail_str_items=[]
    for item in name_list:
        mail_str_items.append(item[1])
    return mail_str_items

def writemails(mail_content,filename):
   with open(filename,'w') as txt_file:
       txt_file.writelines('\n'.join(mail_content))


if __name__=="__main__":
    url="http://forums.threebodytech.com/viewtopic.php?f=12&t=60"
    p=Collect_Email(url)
    p.get_all()
    #print("fuck\n"*10)
    writemails(make_name_mail(p.namelist),"name_email_address_out.txt")
    writemails(make_mail(p.namelist), "email_address_out.txt")

    url = "http://forums.threebodytech.com/viewtopic.php?f=12&t=63"
    p = Collect_Email(url)
    p.get_all()
    writemails(make_name_mail(p.namelist),"name_email_address_in.txt")
    writemails(make_mail(p.namelist), "email_address_in.txt")
