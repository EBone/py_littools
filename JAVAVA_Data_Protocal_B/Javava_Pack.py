import struct
from .info import MessageNames,GameCommand,GameStatus,GameResult
from .base_protocal import Javava_Base_Proto,wordpack

class Task_HeartBeat(Javava_Base_Proto):
    def __init__(self):
        super().__init__(MessageNames.Task_HeartBeat)
    def pack(self):
        headerdata=self.packheader()
        return b''.join([headerdata,wordpack(0x0000)])
    def unpack(self,data_no_header):
        print("Task_HeartBeat Recieved!")
        return True

class Task_Onlog(Javava_Base_Proto):
    def __init__(self):
        super().__init__(MessageNames.Task_Onlog)
    def pack(self,log_content):
        content_data=log_content.encode('utf-8')
        headerdata=self.packheader()
        content_length=len(content_data)
        if content_length<self.message_max_length:
            return b''.join([headerdata,wordpack(content_length),content_data])
        raise ValueError("Message too long")
    def unpack(self,data_no_header):
        datalen=len(data_no_header)
        paramtuple = struct.unpack(str(datalen)+'s',data_no_header)
        paramlist = list(paramtuple)
        return paramlist


class Task_GameStatus_Return(Javava_Base_Proto):
    def __init__(self):
        super().__init__(MessageNames.Task_GameStatus_Return)
    def pack(self,game_id,game_status):
        #game_id needs to be bytes string
        headerdata=self.packheader()
        if game_status in [GameStatus.Excecuting,GameStatus.Failure,GameStatus.Done]:
            content_data = struct.pack('>32sB', game_id, game_status)
            content_length = len(content_data)
            if content_length < self.message_max_length:
                return b''.join([headerdata, wordpack(content_length), content_data])
        raise ValueError("Status not right or Message too long")
    def unpack(self,data_no_header):
        paramtuple = struct.unpack('>32sB', data_no_header)
        paramlist = list(paramtuple)
        return paramlist


class Task_GameResult_Return(Javava_Base_Proto):
    def __init__(self):
        super().__init__(MessageNames.Task_GameResult_Return)
    def pack(self,game_id,game_status,game_result):
        #game_id needs to be bytes string
        headerdata=self.packheader()
        if game_status==GameStatus.Excecuting and game_result==GameResult.Pending:
            content_data=struct.pack('>32sBB',game_id,game_status,game_result)
            content_length=self.check_datalen(content_data)
            if content_length:
                return b''.join([headerdata,wordpack(content_length),content_data])
        elif game_status==GameStatus.Done and game_result in (GameResult.Win,GameResult.Lose):
            content_data=struct.pack('>32sBB',game_id,game_status,game_result)
            content_length = self.check_datalen(content_data)
            if content_length:
                return b''.join([headerdata, wordpack(content_length), content_data])
        raise ValueError("Status not right or Message too long")
    def unpack(self,data_no_header):
        paramtuple = struct.unpack('>32sBB', data_no_header)
        paramlist = list(paramtuple)
        return paramlist

class Task_GamePic_UpLoad(Javava_Base_Proto):
    def __init__(self):
        super().__init__(MessageNames.Task_GamePic_UpLoad)
    def pack(self,game_id,timestamp,game_pic):
        headerdata = self.packheader()
        game_pic_length=str(len(game_pic))+'s'
        content_data=struct.pack('>32sI'+game_pic_length,game_id,timestamp,game_pic)
        content_length = self.check_datalen(content_data)
        if content_length:
            return b''.join([headerdata, wordpack(content_length), content_data])
        raise ValueError("picture data too big ")
    def unpack(self,data_no_header):
        piclen = str(len(data_no_header[36:]))+'s'
        paramtuple = struct.unpack('>32sI'+piclen, data_no_header)
        paramlist = list(paramtuple)
        return paramlist




