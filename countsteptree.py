''''
1111
1111
1111
1111
'''

import time
import sys
#sys.setrecursionlimit(1000000)

totalrc=(6,6)
n=0
#comparetuple
class mytuple:
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def __eq__(self,other):
        if self.a==other.a or self.b==other.b:
            return True
        else:
            return False
#makenodes
class treetwo:
    def __init__(self,middle):
        self.middle=middle
        self.left=(middle[0]+1,middle[1])
        self.right=(middle[0],middle[1]+1)

    def __call__(self):

        templist=[self.left,self.middle,self.right]
        #print(templist)
        for index,value in enumerate(templist):
            if mytuple(*value)==mytuple(*totalrc):
                templist[index]=0
        #print(templist)
        return templist

#递归比较
def compare(temtple):
    if temtple==0:
        global n
        n=n+1
        return
    else:
        templist=treetwo(temtple)()
        compare(templist[0])
        compare(templist[2])


if __name__=="__main__":
    begin = time.time()
    compare((1,1))
    print(n)
    dif=time.time()-begin
    print(dif)
