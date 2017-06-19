import struct
from .info import MessageNames,GameStatus,GameResult,GameCommand

def bytepack(intdata):
    assert isinstance(intdata, int), "value is not int"
    bytedata=struct.pack('>B',intdata)
    return bytedata

def wordpack(intdata):
    assert isinstance(intdata, int), "value is not int"
    wordata=struct.pack('>I',intdata)
    return wordata

class Javava_Base_Proto:
    proto_header=(0xac,0xe0)
    proto_name = 0x01
    # use message_length to check datalength
    message_max_length=(1<<32)-1
    def __init__(self,version_number,message_name):
            #check value and get the bytedata
            self.version_number=bytepack(version_number)
            self.message_name=bytepack(message_name)

    def packheader(self):
        headerdata=b''.join([struct.pack('>B',self.proto_header[0]),struct.pack('>B',self.proto_header[1]),struct.pack('>B',self.proto_name),self.version_number,self.message_name])
        return headerdata

#pack和unpack类
class Javava_Pack(Javava_Base_Proto):
    def pack(self,data):
        raise NotImplementedError

class Javava_Unpack(Javava_Base_Proto):
    #def stripheader(self,data):
     #   return data[(len(self.packheader())+4):]
    def unpack(self,data):
        raise NotImplementedError


if __name__=="__main__":
    pass
