import struct
from .info import MessageNames
from .Javava_Unpack import Task_Game_New,Task_Game_Query
from .Javava_Pack import Task_Onlog,Task_GameStatus_Return,Task_GameStatus_Control,Task_GameResult_Return,Task_Game_Command,Task_GamePic_UpLoad

def unpack_data(data):
	revheader=struct.unpack('>5BI',data[:9])
	if revheader[4]==MessageNames.Task_Game_New:
		paramlist=Task_Game_New(revheader[3]).unpack(data[9:])
	if revheader[4]==MessageNames.Task_Game_Query:
		paramlist=Task_Game_Query(revheader[3]).unpack(data[9:])
	return revheader,paramlist
	
def generate_classdict():
	clslist=[Task_Onlog,Task_GameStatus_Return,Task_GameStatus_Control,Task_GameResult_Return,Task_Game_Command,Task_GamePic_UpLoad]
	namelist=[MessageNames.Task_Onlog,MessageNames.Task_GameStatus_Return,MessageNames.Task_GameStatus_Control,MessageNames.Task_GameResult_Return,MessageNames.Task_Game_Command,MessageNames.Task_GamePic_Upload]
	return dict(zip(namelist,clslist))
	
	
def pack_data(messagename,version_number,*params):
	classdict=generate_classdict()
	if messagename in classdict.keys():		
		return classdict[messagename](version_number).pack(*params)
	
	
		
if __name__=="__main__":
	#print(generate_classdict())
	print(pack_data(0x01,0x01,"fuckthatsfasdfsdfasdfasf补充：1 初始化"))


