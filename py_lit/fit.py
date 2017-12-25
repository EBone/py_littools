import wave
import struct
import numpy as np
import matplotlib.pyplot as plt
wavfile=wave.open("good_16.wav","r")
params=wavfile.getparams()
nchannels, sampwidth, framerate, nframes=params[:4]
strdata=wavfile.readframes(nframes)
numdata=struct.unpack('<'+str(nframes)+'h',strdata)

numdata=[i/32768 for i in numdata[200000:210000]]
print(nframes)
x=np.linspace(0,nframes,nframes)
x=x[200000:210000]

#plt.plot(x,numdata)
#plt.show()

from scipy.optimize import least_squares

def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)

def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)


p0 = [1.0, 198/44100, 0]
plsq = least_squares(residuals, p0,method='trf',loss='linear',tr_solver='exact',args=(numdata, x),verbose=0)
print(plsq.x)
nd=func(x, plsq.x)
#print(nd)
plt.plot(x[:1000], numdata[:1000], label="actual data")
plt.plot(x[:1000],nd[:1000], label="fitting data")
plt.show()



#wavfile.readframes()

