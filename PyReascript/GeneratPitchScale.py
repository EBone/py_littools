
#35-88 B1 E6
#chr  65-72

def generate_PitchName():
    tPitchNamelist = [chr(i) for i in range(65, 72)]
    tPitchNamelist.append(tPitchNamelist[0])
    del tPitchNamelist[0]
    tPitchNamelist.append(tPitchNamelist[0])
    del tPitchNamelist[0]
    PitchNameList = []
    for x, i in enumerate(tPitchNamelist):
        PitchNameList.append(i)
        if x in [0, 1, 3, 4, 5]:
            PitchNameList.append('#' + i)
    return PitchNameList


def generate_semiScale(Startpitch=36):
    pitchdict = {}
    #B1-E6
    temp = Startpitch
    for i in range(2, 7):
        for y in generate_PitchName():

                pitchdict[y + str(i)] = temp
                temp = temp + 1
    pitchdict.update({'B1': 35})
    return pitchdict


if __name__=="__main__":
    #print(generate_PitchName())

    pitchlist=generate_semiScale()
    print(pitchlist)
    print(pitchlist['B3'])






'''
print(PitchNameList)
['B','C']
{'B1':35,}
print(pitchdict)
'''