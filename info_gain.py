import pandas as pd
import numpy as np
from collections import Counter

df = pd.read_csv("balloon_adult.csv",header = None)

df.columns = ["color","size","act","age","inflated"]
#print(df.head())


dict_class = Counter(df.inflated)
print(dict_class)
dict_color = Counter(df.color)

l = len(df)

en_class=0
en_color=0
en_color_y=0
en_color_p=0
for i in dict_class.keys():
    en_class += ((dict_class[i]/l) * np.log2(dict_class[i]/l))

en_class *= -1.0
print(en_class)
df_y = df[df.color == 'YELLOW']
# print(df_t)
df_p = df[df.color == 'PURPLE']

dict_color_y = Counter(df_y['inflated'])
dict_color_p = Counter(df_p['inflated'])

l_y = len(df_y)
l_p = len(df_p)
# print(dict_color_t)
for i in dict_color_y.keys():
    print((dict_color_y[i]/(l_y)) * np.log2(dict_color_y[i]/(l_y)))
    en_color_y += ((dict_color_y[i]/(l_y)) * np.log2(dict_color_y[i]/(l_y)))
en_color_y *= -1.0
print("en_color_y",en_color_y)
for i in dict_color_p.keys():
    print((dict_color_p[i]/(l_p)) * np.log2(dict_color_p[i]/(l_p)))
    en_color_p += ((dict_color_p[i]/(l_p)) * np.log2(dict_color_p[i]/(l_p)))
en_color_p *= -1.0
print("en_color_p",en_color_p)
en_color = ((l_y/l) * en_color_y) + ((l_p/l) * en_color_p)

print(en_class-en_color)
