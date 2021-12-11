import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
print(data)

index = ['large', 'medium', 'small']
random = [862881, 5360, 673]
forceatlas = [7821, 379, 673]
yifanhu = [8759, 372, 115]
reingold = [10110, 394, 141]
df = pd.DataFrame({'random': random, 'forceatlas': forceatlas, 'yifanhu': yifanhu, 'reingold': reingold}, index=index)

print(df)
ax = df.plot.bar(rot=0, logy=True)
plt.ylabel('number of edge crossings')
plt.xlabel('file')
plt.show()


index = ['large', 'medium', 'small']
random = [10957, 418, 0]
forceatlas = [1461, 209, 68]
yifanhu = [2922, 209, 0]
reingold = [1461, 209, 0]
df = pd.DataFrame({'random': random, 'forceatlas': forceatlas, 'yifanhu': yifanhu, 'reingold': reingold}, index=index)

print(df)
ax = df.plot.bar(rot=0, logy=True)
plt.ylabel('number of edge bends')
plt.xlabel('file')
plt.show()