
class WavHandlerBase:
    def __init__(self,dlist):
        self.dlist = dlist
    def handle(self):
        raise NotImplementedError


class Handler_FadeIN(WavHandlerBase):
    def __init__(self,dlist):
        super().__init__(dlist)
    def handle(self):
        data_len=len(self.dlist)
        for x,i in enumerate(self.dlist):
            self.dlist[x]=int(i*(x+1)/data_len)
        return self.dlist


class Handler_FadeOut(WavHandlerBase):
    def __init__(self,dlist):
        super().__init__(dlist)
    def handle(self):
        data_len=len(self.dlist)
        for x,i in enumerate(self.dlist):
            self.dlist[x]=int(i*((data_len-x)/data_len))
        return self.dlist

class Handler_Test(WavHandlerBase):
    def __init__(self,dlist):
        super().__init__(dlist)
    def handle(self):
        return self.dlist
