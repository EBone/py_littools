import mido
import os
datalist=[]
def makearraycode(valuelist,filename):
    datalist.append("int "+filename.split(".")[0]+"["+str(len(valuelist))+"] = "+"{"+",".join(valuelist)+"};\n")
    with open("mididata.cpp","w") as datafile:
        datafile.writelines(datalist)


def get_midimessage(filepath):
    for filename in os.listdir(filepath):
        noteslist=[]
        mf = mido.MidiFile(os.path.join(filepath,filename))
        for tracks in mf.tracks:
            for message in tracks:
                if message.type=="note_on":
                    noteslist.append(str(message.note))
        makearraycode(noteslist,filename)


if __name__=="__main__":
    filepath=r"C:\Users\TBT_E\Desktop\patterns"
    get_midimessage(filepath)







# mf=mido.MidiFile("Part.mid")
# #print(mf.ticks_per_beat)
# n=0
# for tracks in mf.tracks:
#     for i in tracks:
#         if i.type == "note_on":
#             n = n +1
#             print(i.note)
# print("------------------------------")
#
# templist=[]


