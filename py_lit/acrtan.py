import numpy as np
import matplotlib.pyplot as plt
x=[i/100 for i in range(-1000,1000,1)]
print(max(x))
#y=np.arctan(x)/1.5
y=[ i[0]-i[1]for i in zip([i*1.5 for i in x],[pow(tx,3) for tx in x])]
plt.plot(x,y)
plt.show()

# oldvalue=5.0
# newvlue=3.0
#
# for i in range(500):
#     oldvalue=oldvalue*0.99+newvlue*(1-0.99)
#     print(oldvalue)
