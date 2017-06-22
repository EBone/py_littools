import struct
datalike=b'\x00\x00\x02\xff\xff\xff'	#b'\xff\xff\xff\xff\xff\xff'


class Handle_24bit_Data:

	def __init__(self,bytes_data,handle_method):
		self.bytes_data=bytes_data
		self.handle_method=handle_method

	def iter_bytes_data(self):
		datalist=struct.iter_unpack('>BH',self.bytes_data)
		return datalist
		
	def make_int24_value(self,data_tp):
		str_data=''.join([hex(data_tp[0]),hex(data_tp[1])[2:]])
		print(str_data)
		hex_value =int(str_data,base=16)
		return hex_value

	def split_int24(self,hex_num):
		hex_str_nbytes=hex(hex_num)
		print(hex_str_nbytes)
		if len(hex_str_nbytes)>6:	
			hex_str_1bytes=hex_str_nbytes[:-4]
			print(hex_str_1bytes)
			hex_str_2bytes=hex_str_nbytes[-4:]
			return int(hex_str_1bytes,base=16),int(hex_str_2bytes,base=16)
		else:
			return 0,int(hex_str_nbytes,base=16)
	
	def pack_data(self,tp):
		return struct.pack('>BH',*tp)
	
	def __call__(self):
		data_generator=self.iter_bytes_data()
		int24_datalist=map(self.make_int24_value,data_generator)			#get int value list
		handled_data=map(self.handle_method,int24_datalist)					#handle int data
		hex_tuple_list=map(self.split_int24,handled_data)					#split to 8bit and 16bit
		int24_bitdata=map(self.pack_data,hex_tuple_list)
		
		return int24_bitdata
		

if __name__=="__main__":
	def halflower(data):
		return int(data/3) 
		
	print(list(Handle_24bit_Data(datalike,halflower)()))
	
	
	#print(list(hex24_bit_datalist))
	#print(list(handled_data))
	#print(list(hex24_tuple_list))
	#print(list(hex24_bit_data))





