import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##########task 1##########

df1=pd.DataFrame(np.random.randint(1,10,(10,10)))

##########task 2##########

df1.index=['a','b','c','d','e','f','g','h','i','j']
temp_list=[]

for i in df1:
    if np.all(df1.iloc[i]>5):
        temp_list.append(i)

print(df1.iloc[temp_list])

##########task 3##########

df3=pd.DataFrame(np.random.randint(1,10,(10,10)))
df3.index=['a','b','c','d','e','f','g','h','i','j']
df3.columns=['k','l','m','n','o','p','q','r','s','t']

print(df3.shape)
print(df3.columns)
print(df3.mean(axis=None))
df3.to_csv('df3.csv')

##########task 4##########

emojis=pd.read_csv('emojis.csv',index_col='Rank')

print(emojis.loc[1,'Subcategory'])

##########task 5##########

emojis=pd.read_csv('emojis.csv',parse_dates=True)
em=emojis.groupby(['Year']).count()

plt.plot(em.index,em['Rank'])
plt.savefig('1.png')
plt.show