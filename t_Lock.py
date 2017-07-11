from threading import Thread,Lock
import time

class L_A(Thread):
    def __init__(self,lock):
        Thread.__init__(self)
        self.lock=lock
    def run(self):
        self.lock.acquire()
        self.lock.acquire()
        self.lock.acquire()
        print("released")


class L_R(Thread):
    def __init__(self,lock):
        Thread.__init__(self)
        self.lock=lock
    def run(self):
        self.lock.release()
        time.sleep(0.01)
        self.lock.release()

if __name__=="__main__":
    l=Lock()
    a=L_A(l)
    r=L_R(l)
    a.start()
    r.start()
    a.join()
    r.join()



