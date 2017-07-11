from threading import Event
from threading import Thread
import random,time
class t_E_P(Thread):
    def __init__(self,integer,event):
        Thread.__init__(self)
        self.integer=integer
        self.event=event
    def run(self):
        while True:
            a=random.randint(0,100)
            self.integer.append(a)
            print("%d was add to the list by Thread P"%a)
            self.event.set()
            self.event.clear()
            print("cleared by Thread P now,flase")
            time.sleep(1)

class t_E_C(Thread):
    def __init__(self,integer,event):
        Thread.__init__(self)
        self.integer = integer
        self.event = event
    def run(self):
        while True:
            print("fuck")
            if self.integer:
                p=self.integer.pop()
                print("%d was popped by Thread C"%p)
            self.event.wait()

if __name__=="__main__":
    integer=[]
    event=Event()
    p=t_E_P(integer,event)
    c=t_E_C(integer,event)
    p.start()
    c.start()
    p.join()
    c.join()



