import pandas as pd
import matplotlib.pyplot as plt     #I am pretty sure pyplot is the original functionality of matplotlib
import matplotlib.ticker as ticker
import numpy as np
df = pd.read_csv("output/Data.csv")
size = df.shape

k = df['category'].value_counts()
k1 = df['tag'].value_counts()
print( df['pub_date'].value_counts())
OUTPUT_FILENAME = 'output/baocao.txt'
with open(OUTPUT_FILENAME, 'w', encoding='utf8') as f:
    f.write('Kich thuoc: {} '.format(size))
    f.write('\n')
    f.write(' {} '.format(k.to_frame()))
    f.write('\n')
    f.write(' {} '.format(k1.to_frame()))
plt.xlabel('pub_date')
plt.ylabel('Count')
plt.suptitle('Topic')
plt.bar(df['tag'], k1[1],color='red')
plt.show()