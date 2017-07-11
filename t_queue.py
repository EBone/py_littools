from queue import Queue
from threading import Thread
import random,time

class Procuder(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue=queue
        self.i=50
    def run(self):
        while self.i>0:
            value=random.randint(0,10)
            self.queue.put(value)
            print("%d was put in to "%value)
            #print("all been get")
            self.i-=1
        self.queue.join()
        print("thread p done")


class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            value=self.queue.get()
            time.sleep(0.005)
            print("%d get "%value)
            #print("unfinished %d"%self.queue.unfinished_tasks)
            self.queue.task_done()
            if self.queue.unfinished_tasks==0:
                #print("fuck")
                break


if __name__=="__main__":
    q=Queue()
    p=Procuder(q)
    c=Consumer(q)
    p.start()
    c.start()


