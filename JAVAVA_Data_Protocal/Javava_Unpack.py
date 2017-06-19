import struct
from .info import MessageNames
from .base_protocal import Javava_Unpack

class Task_Game_New(Javava_Unpack):
    def __init__(self,version_number):
        super().__init__(version_number,MessageNames.Task_Game_New)
    def unpack(self,data_no_header):
        #data_no_header=self.stripheader(data)
        paramtuple=struct.unpack('>32s32s4I',data_no_header[:80])
        taillength=len(data_no_header[80:])
        paramlist=list(paramtuple)
        paramlist.append(struct.unpack(str(taillength)+'s',data_no_header[80:]))                        #length and other data
        return paramlist

class Task_Game_Query(Javava_Unpack):
    def __init__(self,version_number):
        super().__init__(version_number,MessageNames.Task_GameResult_Query)
    def unpack(self,data_no_header):
        #data_no_header=self.stripheader(data)
        paramtuple=struct.unpack('>I32s',data_no_header)
        paramlist=list(paramtuple)
        return paramlist[1]
