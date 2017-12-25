import codecs
class GetWaParams:
    def __init__(self,rppfile="filter-wah.rpp"):
        self.rppfile=rppfile
        self.param_base64_list=[]
        self.tracklist=[]
        self.paramlist=[]

    def hanlefile(self):
        with open(self.rppfile, "r") as rppfile:
            rppcontent = rppfile.readlines()

            print(rppcontent)
            for x, i in enumerate(rppcontent):
                if ("<TRACK") in i:
                    self.tracklist.append(rppcontent[x + 1].strip())
                if ('<VST "VST: WaWaTTT (yourcompany)" WaWaTTT.dll 0 "" 1379233890') in i:
                    print("hahah")
                    lines = 0
                    tempstr = ""
                    while ">" not in rppcontent[x + lines]:
                        lines += 1
                        tempstr += rppcontent[x + lines].strip().split(">")[0]
                    self.param_base64_list.append(tempstr)

    def decode_params(self):
        decoder_64 = codecs.getdecoder("base64")
        for b64_str in self.param_base64_list:
            rppcode=bytes(b64_str,"ascii")
            normcode = decoder_64(rppcode)
            tempstr = normcode[0].split(b"<")[1].decode("ascii")
            tempstr = tempstr.split("/")[0]
            strlist = tempstr.split(" ")[1:]
            self.paramlist.append(strlist)

    def write_to_file(self):
        with open("reaper_parameter.txt","w") as rf:
            for items in zip(self.tracklist, self.paramlist):
                rf.write(items[0]+"\n")
                for x,param in enumerate(items[1]):
                    templist=param.split('"')
                    if x<6:
                        if x%3==0:
                            rf.write(templist[0][:-1]+"  "+str(float(templist[1])*50.0)+"\n")
                        if x%3==1:
                            rf.write(templist[0][:-1]+"  "+str(float(templist[1])*20.0)+"\n")
                        if x%3==2:
                            rf.write(templist[0][:-1]+"  "+str(float(templist[1])*20000.0)+"\n")
                    else:
                        if x==6:
                            rf.write(templist[0][:-1] + "  " + templist[1] + "\n")
                        if x==7:
                            rf.write(templist[0][:-1] + "  " + str(float(templist[1])*5.0) + "\n")

    def __call__(self):
        self.hanlefile()
        self.decode_params()
        self.write_to_file()



if __name__=="__main__":
    GetWaParams()()
