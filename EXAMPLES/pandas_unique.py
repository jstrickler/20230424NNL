import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../DATA/presidents.xlsx')
df.index = range(1,len(df)+1)

print(df.head())
print(df.loc[1])
party_counts = df['Party affiliation'].value_counts()
# OR party_counts = df.value_counts('Political Party')
print(party_counts)
# plot the data
plt.figure(figsize=(20.0,8.0))
party_counts.plot(kind='barh')
plt.show()
