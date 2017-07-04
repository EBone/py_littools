import wave
from .Handle16BitWave import Handle_16bit_Data
from .Handle24BitWave import Handle_24bit_Data
from .WavHandler import Handler_FadeIN,Handler_FadeOut,Handler_CrossFade



class MakeWave:
    def __init__(self,r_path,p_header,p_tail):
        self.r_wav_file = wave.open(r_path, 'rb')
        self.params = self.r_wav_file.getparams()
        if self.params[1] ==2:
            self.handler=Handle_16bit_Data
        elif self.params[1]==3:
            self.handler=Handle_24bit_Data
        else:
            raise Exception("sampewidth not supported,only support 16 and 24 bits")
        if self.params[0]==2:
            raise Exception("until now only mono supported")
        self.p_header=p_header
        self.p_tail=p_tail

        assert((self.p_header+self.p_tail)<self.get_framelen())

    def get_frames(self):
        str_data_len=self.get_framelen()
        str_data=self.r_wav_file.readframes(str_data_len)
        self.r_wav_file.close()
        if self.p_header==0 and self.p_tail is not 0:
            return str_data[:-self.p_tail],str_data[-self.p_tail:]
        elif self.p_tail==0 and self.p_header is not 0:
            return str_data[:self.p_header],str_data[self.p_header:]
        elif self.p_header==0 and self.p_tail==0:
            return str_data
        else:
            return str_data[:self.p_header],str_data[self.p_header:self.p_tail],str_data[self.p_tail:]

    def get_framelen(self):
        return self.params[3]
    def handle_wav(self):
        raise NotImplementedError

    def write_frames(self,w_path):
        w_wav_file = open(w_path, 'wb')
        w_wav_file.setparams(self.params)
        data = self.handle_wav()
        w_wav_file.writeframesraw(data[0])
        w_wav_file.writeframesraw(data[1])
        w_wav_file.close()



class MakeWave_FadeOut(MakeWave):
    def __init__(self,r_path,p_tail):
        super().__init__(r_path,0,p_tail)
    def handle_wav(self):
        header_data,tail_data=self.get_frames()
        tail_data_h=self.handler(tail_data,Handler_FadeOut)()
        return header_data,tail_data_h


class MakeWave_FadeIn(MakeWave):
    def __init__(self,r_path,p_header):
        super().__init__(r_path,p_header,0)
    def handle_wav(self):
        header_data,tail_data=self.get_frames()
        header_data_h=self.handler(header_data,Handler_FadeIN)()
        return header_data_h,tail_data

class MakeWave_CrossFade:
    def __init__(self,left_wav,right_wav,cross_len):
        #left_wav fadeout
        #righ_wav fadein
        self.left_wav=left_wav
        self.right_wav=right_wav
        self.cross_len=cross_len

    def get_crossfade_data(self):
        wav_fout=MakeWave_FadeOut(self.left_wav,self.cross_len)
        params=wav_fout.params[:3]
        wav_fin=MakeWave_FadeIn(self.right_wav,self.cross_len)
        left_body,left_tail=wav_fout.handle_wav()
        right_header,right_body=wav_fin.handle_wav()
        data_combin=wav_fout.handler(b''.join([left_tail,right_header]),Handler_CrossFade)()
        return left_body,data_combin,right_body,params

    def set_params(self,wav_file,nchannel,sampwidth,framerate):
        wav_file.setnchannels(nchannel)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)

    def write_frames(self,w_path):
        w_wav_file = wave.open(w_path, 'wb')
        data = self.get_crossfade_data()
        self.set_params(w_wav_file,*data[3])
        w_wav_file.writeframesraw(data[0])
        w_wav_file.writeframesraw(data[1])
        w_wav_file.writeframesraw(data[2])
        w_wav_file.close()


if __name__=="__main__":

    #MakeWave_FadeIn("ttt.wav",48000*4).write_frames("tnt.wav",)
    #MakeWave_FadeOut("ttt.wav", 48000 * 4).write_frames("tnt2.wav")
    MakeWave_CrossFade("ttt.wav","ttt.wav",48000*6).write_frames("tcf.wav")








