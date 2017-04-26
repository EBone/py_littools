from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os.path

class SendMail:
    def __init__(self,sender,reciever,title,text=None,pdfpath=None):
        self.sender=sender
        self.title=title
        self.pdfpath=pdfpath
        self.text=text
        self.reciever=reciever

    def pdfattach(self,pdfpath):
        with open(pdfpath,"rb") as pdffile:
            pdfatt=MIMEBase("application","pdf")
            pdfatt.set_payload(pdffile.read())
            print("encoding")
            encoders.encode_base64(pdfatt)
            pdfatt.add_header('content-disposition','attachment',filename=os.path.split(pdfpath)[-1])
            return pdfatt

    def messagetext(self,text):
        Textmessage=MIMEText(text,_charset='utf-8')
        return Textmessage



    def makemessage(self):
        message = MIMEMultipart()
        message["Subject"]=self.title
        message["to"] =self.reciever
        message["from"] = self.sender

        if self.pdfpath:
            message.attach(self.pdfattach(self.pdfpath))
        if self.text:
            message.attach(self.messagetext(self.text))
        return message.as_string()


    def send(self):

        print("setup process")
        session = smtplib.SMTP("smtp.126.com", 25)
        session.login(self.sender, "gk198710225013WL")
        print("login")
        session.sendmail(self.sender, self.reciever,self.makemessage())
        print("sending")
        session.quit()
    def __call__(self):
        print(*sys.argv[1:])
        self.send()




if __name__=="__main__":
    import sys
    myaddr="enone_wxw@126.com"
    #SendMail(myaddr,myaddr,"hahah","hithere,\n  nidaye")()

    SendMail(*sys.argv[1:])()




