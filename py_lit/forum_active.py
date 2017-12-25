import requests
from pyquery import PyQuery as pq
import time

class Forum_active:
    def __init__(self,sid='d139da989557fafc860649bd86288fc4'):
        self.defaulturl="http://forums.threebodytech.com/"
        self.sid=sid
        self.session=requests.session()
        self.adminurl=None
        self.acpsid=None
        self.acpcredential=None
        self.acppayload=None

    def login(self):
        payload={'username':'admin','password':'m_idi2audiO_603','redirect':'./ucp.php?mode=login','sid':self.sid,'login':'Login'}
        rep=self.session.post('http://forums.threebodytech.com/ucp.php?mode=login',data=payload)
        tadmurl=pq(rep.content)(".tab.acp a").attr("href")
        if tadmurl:
            self.adminurl=self.defaulturl+tadmurl
        else:
            print("没获得acp地址")
            raise

    def get_acp_session(self):
        acpres=self.session.get(self.adminurl)
        acpdoc=pq(acpres.content)("input[type='hidden']")
        acppayload={}
        for acp in acpdoc.items():
            temp = pq(acp)
            acppayload[temp.attr("name")] = temp.attr("value")
        self.acpsid = acppayload['sid']
        self.acpcredential = acppayload['credential']
        acppayload['username'] = 'admin'
        acppayload['password_' + self.acpcredential] = 'm_idi2audiO_603'
        acppayload['login'] = 'Login'
        self.acppayload=acppayload

    def get_inactive(self):
        acpres = self.session.post("http://forums.threebodytech.com/adm/index.php?sid=" + self.acpsid, data=self.acppayload)
        redicturl=acpres.__dict__['url']
        res=self.session.get(redicturl+"&i=12")
        return res.content
    def __call__(self):
        self.login()
        self.get_acp_session()
        return self.get_inactive()


if __name__=="__main__":
    content=Forum_active()()
    with open("t.html", "wb") as f:
        f.write(content)
    docfinal = pq(content)(".username")
    if docfinal:
        print(docfinal.text())
    else:
        print(pq(content)("h1").text())
