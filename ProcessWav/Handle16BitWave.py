import struct
# datalike=b'\x00\x00\x02\xff\xff\xff'	#b'\xff\xff\xff\xff\xff\xff'
import audioop

class Handle_16bit_Data:
    def __init__(self, bytes_data, handler):
        self.bytes_data = bytes_data
        self.handler = handler

    def iter_bytes_data(self):
        data_len_str=str(int(len(self.bytes_data)/2))
        print(data_len_str)
        datalist = list(struct.unpack('<'+data_len_str+'h', self.bytes_data))
        return datalist

    def pack_data(self, tp):
        tp_len_str=str(len(tp))
        return struct.pack('<'+tp_len_str+'h', *tp)

    def __call__(self):

        data_tp = self.iter_bytes_data()
        print(data_tp)
        handled_data = self.handler( data_tp).handle()        # handle int data
        return self.pack_data(handled_data)


if __name__ == "__main__":

    import wave
    from  WavHandler import Handler_FadeOut,Handler_Test,Handler_FadeIN
    wavfile=wave.open("t16.wav",'r')
    wav_len=wavfile.getnframes()
    process_len=int(wav_len/2)*2
    str_data=wavfile.readframes(wav_len)
    handled_data=Handle_16bit_Data(str_data[:process_len],Handler_FadeIN)()
    wav_file_w=wave.open("t3t.wav",'wb')
    wav_file_w.setnchannels(1)
    wav_file_w.setsampwidth(2)
    wav_file_w.setframerate(48000)
    wav_file_w.writeframesraw(handled_data)
    wav_file_w.writeframesraw(str_data[process_len:])



# print(list(hex24_bit_datalist))
# print(list(handled_data))
# print(list(hex24_tuple_list))
# print(list(hex24_bit_data))