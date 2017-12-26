
length=0
factorlist=[0]*9
with open(r"C:\Users\TBT_E\MyP\py_littools\py_lit\disdata\Mag60_K.txt","r") as factorfile:
    for num,ft in enumerate(factorfile.read().split(",")):
        factorlist[num]=ft.strip()

datalist=[]
with open(r"C:\Users\TBT_E\MyP\py_littools\py_lit\disdata\Mag60_sub_DCoffset.txt",'r') as disfile:
    strdata=disfile.readlines()
    tl=[]
    for data in strdata:
        t=data.split("\t")
        t[-1]=t[-1].strip()
        tl.append(t)
    length=len(tl)
    datalist=list(zip(*tl))
print(len(datalist[0]))

#新的数据
datawithoutfactor=""
if datawithoutfactor:
    with open(datawithoutfactor,"r") as datanft:
        nftstrdata=datanft.readlines()
        nfttl = []
        for data in strdata:
            nftt = data.split("\t")
            nftt[-1] = nftt[-1].strip()
            nfttl.append(nftt)
        length = len(nfttl)
        datalist.extend(zip(*nfttl))


strdatalist=[]
for x,i in enumerate(datalist):
    strdatalist.append("{"+factorlist[x]+","+"{"+"\n"+",\n".join(i)+"\n"+"}},")

arraystr="const Distdata d_data[4]={\n"
datacontent=arraystr+"".join(strdatalist)+"};\n"
strutype='''
struct Distdata
{
    float  k;
    float data['''+str(length)+'''];

};
'''
with open("disdata.cpp","w") as wdisdata:
    wdisdata.write(datacontent)

with open("disdata.h","w") as wheader:
    wheader.write(strutype)
    wheader.write("extern const Distdata d_data[4];\n")


