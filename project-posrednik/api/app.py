import flask as Flask
from flask import *

app = Flask(__name__)
app.config["DEBUG"]=True
#info: 4 dostawcow, 2 odbiorcow, z blokowaniem tras, export danych do txt?
#webowa, bez interfejsu(bez formularzy do wpisania danych), z wizualizacja danych (wyswietlanie na stronie)


@app.route('/home', methods=['GET'])
def start():
    return render_template("index.html")


@app.route('/posrednik', methods=['GET'])
def posrednik():
    #moze wywolanie metody obliczeniowej? 
    #1 tabela zmienna
    rows=222
    zmienna=333
    #tabela 2 zmienne

    #napisy zmienne
    zysk_posrd=0
    calk_koszt=1
    calk_przychod=2
    return render_template("posrednik.html",rows=rows, zmienna=zmienna,
     calk_przychod=calk_przychod, zysk_posrd= zysk_posrd  , calk_koszt=calk_koszt)


def logistics_method():
    return "idk yet"

app.run()
