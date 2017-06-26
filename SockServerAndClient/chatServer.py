import struct 
import pickle
import socket
import select
import signal
import sys


def send(channel,*args):
	print(args)
	buffer=pickle.dumps(args)
	value=socket.htonl(len(buffer))
	size=struct.pack('L',value)
	channel.send(size)
	channel.send(buffer)


def recieve(channel):
	size=struct.calcsize("L")
	size=channel.recv(size)
	try:
		size=socket.ntohl(struct.unpack("L",size)[0])
	except struct.error as e:
		return ''

	buf=b""
	while len(buf)<size:
		buf=buf+channel.recv(size-len(buf))
	return pickle.loads(buf)[0]


class ChatServer:
	Host='localhost'
	HostName='server'
	def __init__(self,port,backlog):
		self.clients=0
		self.outputs=[]
		self.clientmap={}
		self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.server.bind((self.Host,port))
		print("server listten to port %d"%port)
		self.server.listen(backlog)
		signal.signal(signal.SIGINT,self.sighandler)
	def sighandler(self,signum,frame):
		print("shutting down the server")
		for output in self.outputs:
			output.close()
		self.server.close()

	def get_client_name(self,client):
		info=self.clientmap[client]
		host,name=info[0][0],info[1]
		return "@".join([name,host])
	def run(self):
		inputs=[self.server,sys.stdin]
		self.outputs=[]
		running=True
		while running:
			try:
				readable,writable,exceptional=select.select(inputs,self.outputs,[])
			except select.error as e:
				break
			
			for sock in readable:
				if sock==self.server:
					client,address=self.server.accept()
					print("Chat server: got connection %d from %s"%(client.fileno(),address))
					cname=recieve(client).split("Name:	")[1]
					self.clients+=1
					send(client,"CLient:	"+str(address[0]))
					inputs.append(client)
					self.clientmap[client]=(address,cname)
					msg="\n(Connected: New client (%d) from %s)"%(self.clients,self.get_client_name(client))
					for output in self.outputs:
						send(output,msg)
					self.outputs.append(client)
				if sock==sys.stdin:
					junk=sys.stdin.readline()
					running=False
				else:
					try:
						data=recieve(sock)
						if data:
							msg="\n#["	+self.get_client_name(sock)+']>>'+data
							for output in self.outputs:
								if output!=sock:
									send(output,msg)
						else:
							print("Chat Server:%d hangup"%sock.fileno())
							self.clients-=1
							sock.close()
							inputs.remove(sock)
							self.outputs.remove(sock)
							msg="\n(Now hung up:Client from %s)"%self.get_client_name(sock)
							for output in self.outputs:
								send(output,msg)
					except socket.error as e:
							inputs.remove(sock)
							self.outputs.remove(sock)
		self.server.close()


if __name__=="__main__":
	ChatServer(8888,5).run()










		
		


		

		
