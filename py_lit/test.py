import numpy as np
from scipy.optimize import curve_fit

#创建函数模型用来生成数据
def func(x, a, b):
       return a*x + b

#生成干净数据
x = np.linspace(0, 10, 100)
y = func(x, 1, 2)

#对原始数据添加噪声
yn = y + 0.9 * np.random.normal(size=len(x))

#使用curve_fit函数拟合噪声数据
popt, pcov = curve_fit(func, x, yn)

#输出给定函数模型func的最优参数
print(popt)
print(pcov)
m = np.array([x,np.ones(len(x))])
import pylab as pl
pl.plot(x, y, color="green",label = "actual data")
pl.plot(x, yn, "o", label = "actual data with noise")
pl.plot(x, np.dot(m.T,popt), color="yellow", label = "fitting data")
pl.legend(loc = "best")
pl.show()
