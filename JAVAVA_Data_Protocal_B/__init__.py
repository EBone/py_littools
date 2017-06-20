import struct
from .info import MessageNames
from .Javava_Unpack import Task_Game_New,Task_Game_Query,Task_GameStatus_Control,Task_Game_Command
from .Javava_Pack import Task_Onlog,Task_GameStatus_Return,Task_GameResult_Return,Task_GamePic_UpLoad,Task_HeartBeat

def generate_classdict():
	clslist=[Task_Onlog,Task_GameStatus_Return,Task_GameStatus_Control,\
			 Task_GameResult_Return,Task_Game_Command,\
			 Task_GamePic_UpLoad,Task_HeartBeat,Task_Game_New,Task_Game_Query]
	namelist=[MessageNames.Task_Onlog,MessageNames.Task_GameStatus_Return,\
			  MessageNames.Task_GameStatus_Control,MessageNames.Task_GameResult_Return,\
			  MessageNames.Task_Game_Command,MessageNames.Task_GamePic_UpLoad,\
			  MessageNames.Task_HeartBeat,MessageNames.Task_Game_New,MessageNames.Task_GameResult_Query]
	return dict(zip(namelist,clslist))

classdict=generate_classdict()

def unpack_data(data):
	revheader=struct.unpack('>5BI',data[:9])
	msgname=revheader[4]
	if  msgname in classdict:
		paramlist=classdict[msgname]().unpack(data[9:])
		return revheader,paramlist
	raise ValueError("unpack msgname is not right ")
	
def pack_data(messagename,*params):
	if messagename in classdict:
		return classdict[messagename]().pack(*params)
	raise ValueError("pack msgname is not right")
	
	
		
if __name__=="__main__":
	#print(generate_classdict())
	print(pack_data(0x01,"fuckthatsfasdfsdfasdfasf补充：1 初始化"))


