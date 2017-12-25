import struct
# datalike=b'\x00\x00\x02\xff\xff\xff'	#b'\xff\xff\xff\xff\xff\xff'
import audioop

class Handle_24bit_Data:
    def __init__(self, bytes_data, handler):
        self.bytes_data = bytes_data
        self.handler = handler

    def handle_str_data(self):
        return audioop.byteswap(self.bytes_data,3)

    def iter_bytes_data(self,data):
        datalist = list(struct.iter_unpack('>BH', data))
        return datalist

    def make_int24_value(self, data_tp):
        low_int = data_tp[1]
        low_pos = hex(low_int)[2:]
        low_pos_len = len(low_pos)
        if low_pos_len < 4:
            low_pos =  (4 - low_pos_len) * '0'+low_pos

        str_data = ''.join([hex(data_tp[0]), low_pos])
        hex_value = int(str_data, base=16)
        maxvalue=2<<23
        comvalue=(2<<22)-1
        if hex_value<=comvalue:
            return hex_value
        else:
            return hex_value-maxvalue

    def get_numricdata(self):
        data = self.handle_str_data()
        data_generator = self.iter_bytes_data(data)
        int24_datalist = list(map(self.make_int24_value, data_generator))
        return int24_datalist

    def get_numricdata_handled(self):
        data = self.handle_str_data()
        data_generator = self.iter_bytes_data(data)
        int24_datalist = list(map(self.make_int24_value, data_generator))
        handled_data = self.handler(int24_datalist).handle()
        return handled_data

    def swap_number(self,hexnumber):
        #to change signed value to unsigned
        if hexnumber>=0:
            return hexnumber
        if hexnumber<0:
            return hexnumber+(2<<23)

    def split_int24(self, hex_num):
        hex_str_nbytes = hex(hex_num)
        if len(hex_str_nbytes) > 6:
            hex_str_1bytes = hex_str_nbytes[:-4]
            hex_str_2bytes = hex_str_nbytes[-4:]
            return int(hex_str_1bytes, base=16), int(hex_str_2bytes, base=16)
        else:
            return 0,int(hex_str_nbytes, base=16)

    def pack_data(self, tp):
        return struct.pack('>BH', *tp)

    def __call__(self):
        handled_data = self.get_numricdata_handled()           # handle int data
        swaped_data=map(self.swap_number,handled_data)
        hex_tuple_list = list(map(self.split_int24, swaped_data))  # split to 8bit and 16bit
        int24_bitdata = map(self.pack_data, hex_tuple_list)
        print(int24_bitdata)
        return audioop.byteswap(b''.join(list(int24_bitdata)), 3)


if __name__ == "__main__":

    import wave
    from  WavHandler import Handler_FadeOut,Handler_Test,Handler_FadeIN
    wavfile=wave.open("ttt.wav",'r')
    wav_len=wavfile.getnframes()
    process_len=int(wav_len/2)*3
    str_data=wavfile.readframes(wav_len)
    handled_data=Handle_24bit_Data(str_data[:process_len],Handler_FadeIN)()
    wav_file_w=wave.open("t3t.wav",'wb')
    wav_file_w.setnchannels(1)
    wav_file_w.setsampwidth(3)
    wav_file_w.setframerate(48000)
    wav_file_w.writeframesraw(handled_data)
    wav_file_w.writeframesraw(str_data[process_len:])



# print(list(hex24_bit_datalist))
# print(list(handled_data))
# print(list(hex24_tuple_list))
# print(list(hex24_bit_data))