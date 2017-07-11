import random,time
import threading
from threading import Condition

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, integers, condition):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition
        print("threading-1 created")

    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()
            print('condition acquired by %s' % self.name)
            self.integers.append(integer)
            print ('%d appended to list by %s' % (integer, self.name))
            print ('condition notified by %s' % self.name)
            self.condition.notify()
            print( 'condition released by %s' % self.name)
            self.condition.release()
            time.sleep(1)


class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, integers, condition):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition
        print("threading-2 created")

    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            print("thread2 befor acquire")
            self.condition.acquire()
            print( 'condition acquired by %s' % self.name)
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print( '%d popped from list by %s' % (integer, self.name))
                    break
                print ('condition wait by %s' % self.name)
                self.condition.wait()
                print("thread2 after wait")
            print ('condition released by %s' % self.name)
            self.condition.release()


def main():
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)
    t1.start()
    print("t1 started")
    t2.start()
    print("t2 started")
    time.sleep(3)
    for i in range(10):
        print("fuck")

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
