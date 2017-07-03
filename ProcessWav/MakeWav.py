import wave


class MakeWave:
    def __init__(self,wavpath,handler,p_header,length,p_tail):
        self.wav_file = wave.open(wavpath, 'rb')
        self.handler=handler
        self.p_header=p_header
        self.p_tail=p_tail
        self.p_len=length

    def get_frames(self):
        str_data_len=self.wav_file.getnframes()
        str_data=self.wav_file.readframes(str_data_len)
        if self.p_header==0:
            return str_data[:self.p_len]
        elif self.p_tail==0









