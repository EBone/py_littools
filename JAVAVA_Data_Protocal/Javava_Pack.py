import struct
from info import MessageNames,GameCommand,GameStatus,GameResult
from base_protocal import Javava_Pack,wordpack

class Task_onlog(Javava_Pack):
    def __init__(self,version_number):
        super().__init__(version_number,MessageNames.Task_Onlog)
    def pack(self,log_content):
        content_data=log_content.encode('utf-8')
        headerdata=self.packheader()
        content_length=len(content_data)
        if content_length<self.message_max_length:
            return b''.join([headerdata,wordpack(content_length),content_data])
        raise ValueError("Message too long")

class Task_GameStatus_Return(Javava_Pack):
    def __init__(self,version_number):
        super().__init__(version_number,MessageNames.Task_GameStatus_Return)
    def pack(self,game_id,game_status):
        #game_id needs to be bytes string
        headerdata=self.packheader()
        if game_status==GameStatus.Excecuting:
            content_data=struct.pack('>32sB',game_id,game_status)
            content_length=len(content_data)
            if content_length<self.message_max_length:
                return b''.join(headerdata,wordpack(content_length),content_data)
        elif game_status==GameStatus.Failure:
            content_data=struct.pack('>32sB',game_id,game_status)
            content_length=len(content_data)
            if content_length<self.message_max_length:
                return b''.join(headerdata,wordpack(content_length),content_data)
        elif game_status==GameStatus.Done:
            content_data=struct.pack('>32sB',game_id,game_status)
            content_length=len(content_data)
            if content_length<self.message_max_length:
                return b''.join(headerdata,wordpack(content_length),content_data)
        raise ValueError("Status not right or Message too long")

class Task_GameStatus_Control(Javava_Pack):
    def __init__(self,version_number):
        super().__init__(version_number,MessageNames.Task_GameStatus_Control)
    def pack(self,game_id,game_status):
        #game_id needs to be bytes string
        headerdata=self.packheader()
        if game_status==GameStatus.Done:
            content_data=struct.pack('>32sB',game_id,game_status)
            content_length=len(content_data)
            if content_length<self.message_max_length:
                return b''.join(headerdata,wordpack(content_length),content_data)
        raise ValueError("Status not right or Message too long")

class Task_GameResult_Return(Javava_Pack):
    def __init__(self,version_number):
        super().__init__(version_number,MessageNames.Task_GameResult_Return)
    def pack(self,game_id,game_status,game_result):
        #game_id needs to be bytes string
        headerdata=self.packheader()
        if game_status==GameStatus.Excecuting and game_result==GameResult.Pending:
            content_data=struct.pack('>32sBB',game_id,game_status,game_result)
            content_length=len(content_data)
            if content_length<self.message_max_length:
                return b''.join(headerdata,wordpack(content_length),content_data)
        elif game_status==GameStatus.Done and game_result in (GameResult.Win,GameResult.Lose):
            content_data=struct.pack('>32sBB',game_id,game_status,game_result)
            content_length=len(content_data)
            if content_length<self.message_max_length:
                return b''.join(headerdata,wordpack(content_length),content_data)
        raise ValueError("Status not right or Message too long")

class Task_Game_Command(Javava_Pack):
    def __init__(self,version_number):
        super().__init__(version_number,MessageNames.Task_Game_Comman)
    def pack(self,game_id,timestamp,game_command):
        headerdata = self.packheader()
        for command in GameCommand.getcommand():
            if command == game_command:
                content_data = struct.pack('>32sIB', game_id, timestamp, game_command)
                content_length = len(content_data)
                if content_length < self.message_max_length:
                    return b''.join(headerdata, wordpack(content_length), content_data)
        raise ValueError("Command not right or Message too long")


class Task_GamePic_UpLoad(Javava_Pack):
    def __init__(self,version_number):
        super().__init__(version_number,MessageNames.Task_GamePic_Upload)
    def pack(self,game_id,timestamp,game_pic):
        headerdata = self.packheader()
        game_pic_length=str(len(game_pic))+'s'
        content_data=struct.pack('>32sI'+game_pic_length,game_id,timestamp,game_pic)
        content_length = len(content_data)
        if content_length < self.message_max_length:
            return b''.join([headerdata, wordpack(content_length), content_data])
        raise ValueError("picture data too big ")