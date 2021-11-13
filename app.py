

from flask import Flask
from flask import render_template
import jyserver.Flask as jsf
import numpy as np
import pandas as pd 



app = Flask(__name__)  

@jsf.use(app)
class App:
    # def __init__(self):
    
    
    def test(self):
        syd=pd.read_csv('diffsydiw.csv').dropna()
        dia=pd.read_csv('dia_t.csv').dropna()
        sym=pd.read_csv('sym_t.csv').dropna()

        
        print(sym.head())
        print(dia.head())


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
    app.run()




