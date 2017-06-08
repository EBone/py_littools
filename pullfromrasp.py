import paramiko
import os


#makedir
class Get_SNTPFiles:
    def __init__(self,host,port,remotepath):
        self.host=host
        self.port=port
        self.remotepath=remotepath
        self.localpath=os.getcwd()
        self.transport=paramiko.Transport((host,port))
        self.transport.connect(username='pi',password='raspberry')
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def get_endfix(self,pathname):
        return pathname.split('/')[-1]

    def check_files(self,remotepath,localpath):
        files=''
        try:
            files = self.sftp.listdir(remotepath)
            #'/home/pi/e/SocketThings'
        except IOError:
            pass                  #todo:sntpget文件
        if files:
            print(files)
            if localpath is not self.localpath:
                if not os.path.exists(localpath):
                    os.mkdir(localpath)
            for i in files:
                print(i)
                self.check_files(remotepath+r'/'+i,os.path.join(localpath,i))
        else:
            print((remotepath,localpath))
            self.sftp.get(remotepath, localpath)
    def __call__(self):
        self.check_files(self.remotepath,self.localpath)


if __name__=="__main__":
    import argparse
    argps=argparse.ArgumentParser(description="HostArgparse")
    argps.add_argument('--host',action='store',dest='host',required=False)
    argps.add_argument('--port', action='store', dest='port',type=int, required=False)
    argps.add_argument('--remotepath', action='store', dest='remotepath', required=False)
    given_args=argps.parse_args()

    Host =given_args.host                                                                           # 192.168.31.107
    port = given_args.port                                                                          #22
    Get_SNTPFiles(Host,port,'/home/pi/e')()                                         #'/home/pi/e
