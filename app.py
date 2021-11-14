

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
        output = []
        self.symptom = str(self.js.document.getElementById("sym").value)
       
        syd=pd.read_csv('diffsydiw.csv').dropna()
        dia=pd.read_csv('dia_t.csv').dropna()
        sym=pd.read_csv('sym_t.csv').dropna()
        
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
            self.js.document.getElementById('five').innerHTML = "5." + output[4]


            for item in output:
                goog_search = "https://www.google.com/search?q="+item+"&rlz=1C1RXQR_enCA929CA929&oq=asdasdasd&aqs=chrome..69i57j0i10l3j46i10i175i199j0i10l5.3408j0j9&sourceid=chrome&ie=UTF-8"
                r = requests.get(goog_search)
                soup = BeautifulSoup(r.text, "html.parser")
                print(soup.find('cite').text)

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




