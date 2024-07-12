import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data2.csv')
print(df.columns)
a=[5,9,6,3,9,5]
b=[4,5,7,92,4,2]
plt.figure(figsize=(10,4))
p=plt.subplot(1,2,1)
c=plt.subplot(1,2,2)
p.plot(a,b,c='b',marker='*',markeredgecolor='y',markerfacecolor='r',markersize=30)
c.plot(a,b,c='m',marker='*',markeredgecolor='m',markerfacecolor='y',markersize=30)
plt.xlabel("Box Plot")
plt.ylabel("Category")
plt.title("Box Design")
plt.suptitle("The Advance level Value Showing")
plt.legend("P")
plt.show()