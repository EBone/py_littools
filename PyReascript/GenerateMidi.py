from reaper_python import *
from info import MediaItemInfo
from GeneratPitchScale import generate_semiScale

pitchdict=generate_semiScale()

def print_msg(*msg):
    for i in msg:
        RPR_ShowConsoleMsg("".join([str(i), '\n']))

class GetMediaTake:
    def __init__(self,project,itemnumber,iteminfo):
        self.project=project
        self.itemnumber=itemnumber
        self.iteminfo=iteminfo

    def Get_select_MediaItem(self,project,itemnumber):
        MediaItem = RPR_GetSelectedMediaItem(project, itemnumber)
        return MediaItem


    def Get_select_takeValue(self,MediaItem,ItemInfo):
        takevalue = RPR_GetMediaItemInfo_Value(MediaItem, ItemInfo)
        return takevalue

    def Get_select_takeId(self,MediaItem,take):
        takeid = RPR_GetMediaItemTake(MediaItem, int(take))
        return takeid


    def gettake(self):
        MediaItem=self.Get_select_MediaItem(self.project,self.itemnumber)
        takeid=int(self.Get_select_takeValue(MediaItem,self.iteminfo))
        take=self.Get_select_takeId(MediaItem,takeid)
        return take
'''
class GenerateMidiNote:
    def __init__(self,selectedtakes,generateMethod):
        self.selectedtake=selectedtakes
        self.generateMethod=generateMethod

    def generate(self):
        generateMethod()

class MidiMethodManger:
    def __init__(self,argvs):
'''

def method1(take,startpitch,stoppitch,pitch_interval):
    stkeynum=pitchdict[startpitch]
    spkeynum=pitchdict[stoppitch]

    for i in range(spkeynum-stkeynum):
        RPR_MIDI_InsertNote(take, 0, 0, 1000 * i * 2, 1000 * (1 + 2 * i), 0, stkeynum + i, 120, 0)
        RPR_MIDI_InsertNote(take, 0, 0, 1000 * (i * 2 + 1), 1000 * (2 * (i + 1)), 0, stkeynum+pitch_interval + i, 120, 0)








if __name__=="__main__":


    method1(GetMediaTake(0,0,MediaItemInfo.I_CURTAKE).gettake(),'B1','B3',4)
    method1(GetMediaTake(0, 1, MediaItemInfo.I_CURTAKE).gettake(), 'E2', 'E4', 4)
    method1(GetMediaTake(0, 2, MediaItemInfo.I_CURTAKE).gettake(), 'A2', 'A4', 4)
    '''
    take=GetMediaTake(0,0,MediaItemInfo.I_CURTAKE).gettake()
    for i in range(100):
        RPR_MIDI_InsertNote(take, 0, 0, 1000 * i * 2, 1000 * (1 + 2 * i), 0, 30 + i, 120, 0)
        RPR_MIDI_InsertNote(take, 0, 0, 1000 * (i * 2 + 1), 1000 * (2 * (i + 1)), 0, 37 + i, 120, 0)
    '''