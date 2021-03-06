import numpy as np
from scipy import optimize    # 从scipy库引入optimize模块

X = np.array([ 8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78 ])
Y = np.array([ 7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05 ])

def residuals(p):
        #计算以p为参数的直线和原始数据之间的误差
        k, b = p
        return Y-(k*X+b)

# leastsq()使得residuals()的输出数组的平方和最小，参数的初始值为[1, 0]
r = optimize.leastsq(residuals, [1,0])
k, b = r[0]
print("k=", k, "b=", b)
import pylab as pl
pl.plot(X, Y, "o", label = "actual data")
pl.plot(X, k*X+b, label = "fitting data")
pl.legend(loc = "best")
pl.show()
