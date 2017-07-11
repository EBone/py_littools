import threading,random
from threading import Barrier,Thread
from threading import Condition,Lock

class Barrier_sum(Barrier):
    def __init__(self, parties, action=None, timeout=None):
        super().__init__(parties,action=action,timeout=timeout)
        self.args = (0, 0, 0)

    def _release(self):
        try:
            if self._action:
                self._action(*self.args)
            # enter draining state
            self._state = 1
            self._cond.notify_all()
        except:
            # an exception during the _action handler.  Break and reraise
            self._break()
            raise

class t_B(Thread):
    def __init__(self,barrier,d_list):
        Thread.__init__(self)
        self.barrier=barrier
        self.d_list=d_list
    def run(self):
        #integer=random.randint(0,10)
        l_integer=random.randint(0,2)
        self.d_list[l_integer] =self.d_list[l_integer]+1
        print(self.d_list)
        self.barrier.args=(self.d_list[0],self.d_list[1],self.d_list[2])
        self.barrier.wait()
        print("%d quite"%threading.get_ident())

if __name__=="__main__":
    def fuck(a,b,c):
        print("sum value is %d"%(a+b+c))
        return a+b+c

    b_list = [1, 2, 3]
    t_list=[]
    barrier=Barrier_sum(3,action=fuck)

    for i in range(36):
        t_list.append(t_B(barrier,b_list))
    for b in t_list:
        b.start()
    for b in t_list:
        b.join()



'''
import time
from threading import Thread,Semaphore

class Barrier:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.mutex = Semaphore(1)
        self.barrier = Semaphore(0)

    def wait(self):
        self.mutex.acquire()
        self.count = self.count + 1
        print(self.count)
        self.mutex.release()
        if self.count == self.n: self.barrier.release()
        self.barrier.acquire()
        self.barrier.release()

b = Barrier(2)

def func1():
    time.sleep(3)
    #
    b.wait()
    #
    print('Working from func1')
    return

def func2():
    time.sleep(5)
    #
    b.wait()
    #
    print('Working from func2')
    return

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
'''

