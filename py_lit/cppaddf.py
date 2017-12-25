
import os
filedirs=os.listdir(os.getcwd())
for wafile in filedirs:
    with open(wafile,"r") as wahfile:
        contentlist=wahfile.readlines()
    for x,line in enumerate(contentlist):
        if "." not in line:
            line=line.strip()+".0"
        contentlist[x]=line.strip()+"f;\n"
    with open(wafile,"w") as wahfile:
        wahfile.writelines(contentlist)
    print(contentlist)
