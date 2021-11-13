import numpy as np
import pandas as pd 




syd=pd.read_csv('diffsydiw.csv').dropna()
dia=pd.read_csv('dia_t.csv').dropna()
sym=pd.read_csv('sym_t.csv').dropna()

print(sym.head())
print(dia.head())

print(syd[syd['syd']==2].sort_values('wei',ascending=False).head())
print(dia[dia['did']==56])


print(syd[syd['did']==56])
print(sym[sym['syd']==128])
print(sym[sym['syd']==264])

print(syd[syd['syd']==128].sort_values('wei',ascending=False).head())
print(dia[dia['did']==54])
print(dia[dia['did']==159])
print(dia[dia['did']==177])
print(dia[dia['did']==192])