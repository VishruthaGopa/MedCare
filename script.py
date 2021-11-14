# import numpy as np
# import pandas as pd 

import requests
from bs4 import BeautifulSoup

item = "cough"
html = requests.get('https://www.google.com/search?q=ice cream').text
soup = BeautifulSoup(html, 'html.parser')

# locating .tF2Cxc class
# calling for <a> tag and then calling for 'href' attribute
link = soup.select('.yuRUbf a')['href']
print(link)


# syd=pd.read_csv('diffsydiw.csv').dropna()
# dia=pd.read_csv('dia_t.csv').dropna()
# sym=pd.read_csv('sym_t.csv').dropna()

# # print(sym.head())
# # print(dia.head())

# inp = 4

# test = syd[syd['syd']==2].sort_values('wei',ascending=False)['did']
# print(test.iloc[0])
# for i in range(5):
#     print(dia[dia['did']==test.iloc[i]])

# symp = "Lowe"
# print(sym[sym['symptom'].str.contains(symp)]) 
# # print(syd[syd['did']==22])
# # print(sym[sym['syd']==128])
# # print(sym[sym['syd']==264])

# # print(syd[syd['syd']==128].sort_values('wei',ascending=False).head())
# # print(dia[dia['did']==54])
# # print(dia[dia['did']==159])
# # print(dia[dia['did']==177])
# # print(dia[dia['did']==192])