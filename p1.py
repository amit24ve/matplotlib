import pandas as pd
import matplotlib.pyplot as mp

r=pd.read_csv('data2.csv')
df=r.plot(kind='bar',color='r')
df.legend(loc=1)
mp.xlabel("X axis")
mp.ylabel("Y axis")
mp.title("KDE")
mp.suptitle("HELLO")
mp.show()

import numpy as np

data ={
    'a':[2,3,4,5,5],
    'b':[5,7,8,9,5],
    'c':[9,8,5,3,2]
}
c=pd.DataFrame(data)
print(c.info())
data=np.array([3,4,5,6,7])
data1=np.array([9,7,5,6,3])
mp.subplot(2,1,1)
mp.plot(data,data1)

data=np.array([7,6,5,4,3])
data1=np.array([9,8,7,5,3])
mp.subplot(2,1,2)
mp.plot(data,data1)
a=mp.figure()
a.set_figheight(6)
a.set_figwidth(4)
p=mp.plot(data,data1,color='r',markersize=10,marker='o',markeredgecolor='green',markerfacecolor='yellow')
mp.legend(loc=2)
mp.show()
