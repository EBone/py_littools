import socket
import struct
import sys
import select
from chatServer import recieve,send

Server_Host='localhost'

class chatClient:
	def __init__(self,name,port,host=Server_Host):
		self.name=name
		self.host=host
		self.connected=False
		self.port=int(port)
		self.prompt='['+'@'.join([name,socket.gethostname().split('.')[0]])+']>'
		try:
			self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			self.sock.connect((self.host,self.port))
			print("Now connected to chat server @port %d"%self.port)
			self.connected=True
			send(self.sock,"Name: "+self.name)
			data=recieve(self.sock)
			addr=data.split('CLient: ')[1]
			self.prompt='['+'@'.join([self.name,addr])+']>'
		except socket.error as e:
			print(e)
			print("Failed to connect to chat server @port %d"%self.port)
			sys.exit(1)
	def run(self):
		while self.connected:
			try:
				sys.stdout.write(self.prompt)
				sys.stdout.flush()
				readable,writable,exceptional=select.select([0,self.sock],[],[])
				for sock in readable:
					if sock==0:
						data=sys.stdin.readline().strip()
						if data:
							send(self.sock,data)
					elif sock==self.sock:
						data=recieve(self.sock)
						if not data:
							print("client shutting down")
							self.connected=False
							break
						else:
							sys.stdout.write(data+'\n')
							sys.stdout.flush()
			except KeyboardInterrupt:
				print("Client Interrupted")
				self.sock.close()
				break
if __name__=="__main__":
	chatClient(sys.argv[1],sys.argv[2]).run()



