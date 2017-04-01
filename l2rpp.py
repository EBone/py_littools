#use oneline:
# python -c
#  "import sys;a=[i.strip() for i in sys.stdin.readlines() if 'MARKER' in i];b=[i.split(' ')[2] for i in a];c=map(lambda x:str(int(float(x))/3600)+':'+str((int(float(x))/60)%60)+':'+str(int(float(x))%60),b);print c"
# <_listening_ideaharm_0.17.rpp

from tkinter import Frame,Button,Text,mainloop,BOTH,YES,Tk,filedialog,END,INSERT

import re


def rtime(seconds):
    temp_f=float(seconds)
    temp_i=int(temp_f)
    #print(temp_i)
    ts=temp_i%60

    tm=int(temp_i/60)%60
    th=int((temp_i/60)/60)
    return str(th)+':'+str(tm)+':'+str(ts)



def getMarkPoint(fname):

    if fname:
        rppfile=open(fname,'r')
        strl=[x.strip() for x in rppfile.readlines() if "MARKER" in x ]
        print(strl)

        patterns=r'(MARKER) (\d+) (\d+\.\d+|\d+) (""|.+) \d+ \d+ \d+ R'

        pattern2m=re.compile(patterns)
        result2S=""
        for i in strl:
            tempresult=pattern2m.match(i)
            if tempresult:
                templ=[]

                templ.append(tempresult.group(2))
                templ.append(rtime(tempresult.group(3)))
                templ.append(tempresult.group(4))
                print(" ".join(templ))
                result2S=result2S+" ".join(templ)+'\n'
        return result2S


class Application(Frame):

    def getfname(self):
        options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'D:\公司\reaper'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = None
        options['title'] = 'This is a title'
        fname=filedialog.askopenfilename(**options)
        if fname:
            self.content.delete(1.0, END)
            self.content.insert(INSERT, getMarkPoint(fname))


    def creatWidgets(self):
        self.button=Button(self,text="Click2ChoosePath",width=20,command=self.getfname)
        self.button.pack(expand=YES,fill=BOTH)
        self.content=Text(self)
        self.content.pack(expand=YES, fill="both")

    def __init__(self,master=None):
        super().__init__(master)
        master.title("FindMarkerInRpp")
        self.creatWidgets()
        self.pack(expand=YES,fill=BOTH)

if __name__=="__main__":
    tk=Tk()
    app=Application(tk)
    import subprocess
    p = subprocess.Popen(r'python D:\DjangoProject\untitled4\tkcanvas2.py', shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #p.communicate()
    app.mainloop()

    subprocess.Popen.send_signal(si)


