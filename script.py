import numpy as np
import pandas as pd 

import requests
from bs4 import BeautifulSoup

syd=pd.read_csv('./csv-files/diffsydiw.csv').dropna()
dia=pd.read_csv('./csv-files/dia_t.csv').dropna()
sym=pd.read_csv('./csv-files/sym_t.csv').dropna()


text =[]
# Automatically find a link to mayoclinic - a reputable site I think
item = "acute liver disease"
html = requests.get('https://www.google.com/search?q='+item).text
soup = BeautifulSoup(html,"html.parser")
link = ""
for a in soup.find_all('a',  href = True):
    if("mayoclinic.org/diseases" in str(a)):
        print(a)
        link = str(a)
        break
cutoff = str(a).index('&')
print(cutoff)
print (link[16:cutoff])
newlink = link[16:cutoff]


# With The link, scrape the overview of the disease
html = requests.get(newlink).text
soup = BeautifulSoup(html,"html.parser")
link = ""
divs = soup.find_all("div", {"class": "content"})
p = soup.find_all("p")
for item in p:
    text.append(item)

for i in range(2,5):
    print (*list(filter(lambda a: a != "<p>", text[i])))









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