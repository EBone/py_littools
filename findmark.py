
#use oneline:
# python -c
#  "import sys;a=[i.strip() for i in sys.stdin.readlines() if 'MARKER' in i];b=[i.split(' ')[2] for i in a];c=map(lambda x:str(int(float(x))/3600)+':'+str((int(float(x))/60)%60)+':'+str(int(float(x))%60),b);print c"
# <_listening_ideaharm_0.17.rpp


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

        patterns=r'(MARKER) (\d+) (\d+\.\d+|\d+) (""|\.+) '

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

if __name__=="__main__":
    pass



