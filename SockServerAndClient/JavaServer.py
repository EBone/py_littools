import socket
import select
import struct
import signal
import sys

def recieve(channel):
    data=channel.recv(7)
    msg=struct.unpack('>5BH',data)
    contentlen=msg[5]
    datacontent=channel.recv(contentlen)
    #content=struct.unpack('>'+str(contentlen)+'s',datacontent)[0]
    #messagename=struct.unpack('>B',msg[4])[0]

    return data+datacontent

def send(channel,data):
    channel.send(data)


class JavavaServer:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.outputs=[]
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server.bind((self.host,self.port))
        print("Server started")
        self.server.listen(3)
        print("listening at %s")
        signal.signal(signal.SIGINT,self.signhandler())

    def signhandler(self):
        print("shutting down the server...")
        for output in self.outputs:
            output.close()
        self.server.close()

    def run(self):
        self.inputs=[self.server,sys.stdin]







