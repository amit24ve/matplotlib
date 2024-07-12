import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
fig=plt.figure()
fig.subplots_adjust(left=0.2,right=0.3,top=0.2,bottom=0.1)
a=np.arange(0,20)
b=a*2
x=fig.add_axes([0.2,0.5,0.1,0.2])
fig,x=plt.subplots(nrows=2,ncols=2)
x[0][0].plot(a,b)
x[0][1].plot(a,b)
x[1][0].plot(a,b)
x[1][1].plot(a,b)
fig.suptitle("hello mt")
y=fig.add_axes([0.2,0.5,0.2,0.2])
x=plt.subplot(1,2,1)
x.plot(a,b,color='r',lw=3)
y=plt.subplot(1,2,2)
y.hist(a,b,color='b',lw=3,linestyle='dotted')
plt.show()

axes=fig.subplots(nrows=2,ncols=2)
axes[0][0].plot(a,b)
axes[1][0].plot(a,b)
axes[0][1].plot(a,b)
axes[1][1].plot(a,b)
plt.show()
a=['a','b','c','d']
b=[30,30,25,15]
c=['r','g','b','y']
e=[0.2,0.1,0.3,0.5]
x=plt.subplot(1,2,1)
x.pie(b,labels=a,colors=c,explode=e)
x=plt.subplot(1,2,2)
x.pie(b,labels=a,colors=c,explode=e)
plt.legend(loc='upper right')
plt.show()



import pandas as pd

data = {
  "Duration": [50, 40, 45],
  "Pulse": [109, 117, 110],
  "Calories": [409.1, 479.5, 340.8]
}

df = pd.DataFrame(data)
tc=df.corr()
sns.heatmap(tc,annot=False)
plt.show()