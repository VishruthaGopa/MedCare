

from flask import Flask
from flask import render_template
import jyserver.Flask as jsf
import numpy as np
import pandas as pd 
import re
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)  

@jsf.use(app)
class App:
    def __init__(self):
        self.symptom = ""
    
        

    def test(self):
        # reset dropdowns
        self.js.document.getElementById('dropOne').innerHTML = ""
        self.js.document.getElementById('dropTwo').innerHTML = ""
        self.js.document.getElementById('dropThree').innerHTML = ""
        self.js.document.getElementById('dropFour').innerHTML = ""

        output = []
        self.symptom = str(self.js.document.getElementById("sym").value)
       
        syd=pd.read_csv('./csv-files/diffsydiw.csv').dropna()
        dia=pd.read_csv('./csv-files/dia_t.csv').dropna()
        sym=pd.read_csv('./csv-files/sym_t.csv').dropna()
        
        diseases = sym[sym['symptom'].str.contains(self.symptom, flags=re.IGNORECASE)]
    
        if not diseases.empty:
            sympID = diseases["syd"].iloc[0]
            test = syd[syd['syd']==sympID].sort_values('wei',ascending=False)['did']
            for i in range(4):
                output.append(dia[dia['did']==test.iloc[i]]['diagnose'].iloc[0])

            self.js.document.getElementById('message').innerHTML = "Here are some common diseases that have \"" +diseases["symptom"].iloc[0] + "\" as a symptom."
            self.js.document.getElementById('one').innerHTML =" 1." + output[0]
            self.js.document.getElementById('two').innerHTML = "2." + output[1]
            self.js.document.getElementById('three').innerHTML = "3." + output[2]
            self.js.document.getElementById('four').innerHTML = "4." + output[3]
            
            def findInfo(item,index):
                text =[]
                out = []

                print(item)
                # Automatically find a link to mayoclinic - a reputable site I think
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
                
                # With the link, scrape the overview of the disease
                html = requests.get(newlink).text
                soup = BeautifulSoup(html,"html.parser")
                link = ""
             
                # divs = soup.find_all("div", {"class": "content"})
                p = soup.find_all("p")
                for item in p:
                    text.append(item)

                for i in range(4,7):
                    out.append(list(filter(lambda a: a != "<p>", text[i])))  

                if index == 0:
                    self.js.document.getElementById('dropOne').innerHTML = str(*out[0])+str(*out[1])+str(*out[2])
                elif index == 1:
                    self.js.document.getElementById('dropTwo').innerHTML = str(*out[0])+str(*out[1])+str(*out[2])
                elif index == 2:
                    self.js.document.getElementById('dropThree').innerHTML = str(*out[0])+str(*out[1])+str(*out[2])
                else:
                    self.js.document.getElementById('dropFour').innerHTML = str(*out[0])+str(*out[1])+str(*out[2])

            for count, items in enumerate(output):
                if ":" in items:
                    idx = items.index(":")
                else:
                    idx = len(items)
                findInfo(items[:idx],count)  
            

            
        else:
            self.js.document.getElementById('message').innerHTML = "Sorry, we could not find any diseases with that symptom. Please retry or check your spelling!"
            self.js.document.getElementById('one').innerHTML = ""
            self.js.document.getElementById('two').innerHTML = ""
            self.js.document.getElementById('three').innerHTML = ""
            self.js.document.getElementById('four').innerHTML = ""
            self.js.document.getElementById('five').innerHTML = ""
    

     

@app.route("/")
def index():
    return App.render(render_template("index.html"))

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """

if __name__ == '__main__':
    app.run(debug=True)




