import flask as Flask
from flask import *

app = Flask(__name__)
app.config["DEBUG"]=True
#info: 4 dostawcow, 2 odbiorcow, z blokowaniem tras, export danych do txt?
#webowa, bez interfejsu(bez formularzy do wpisania danych), z wizualizacja danych (wyswietlanie na stronie)


array =[{"onecolumn": 000 , "2ndcolumn": 111},
{"onecolumn": 000 , "2ndcolumn": 111},
{"onecolumn": 000 , "2ndcolumn": 111}]


@app.route('/home', methods=['GET'])
def start():
   # return 'hello '  
    return render_template("index.html")


@app.route('/posrednik', methods=['GET'])
def posrednik():
    #moze wywolanie metody obliczeniowej? 
    return render_template("posrednik.html", array=array)


def logistics_method():
    return "idk yet"

app.run()
