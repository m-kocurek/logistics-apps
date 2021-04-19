import flask as Flask
from flask import *
import main
from main import main_
app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/home', methods=['GET'])
def start():
    return render_template("index.html")


@app.route('/posrednik', methods=['GET'])
def posrednik():
    #Tabela zysków jednostkowych 
    kt = [[0, 0,0], [0, 0,0], [0, 0,0], [0,0,0],[0,0,0]]
    #Tabela optymalnych przewozów
    tab_opt=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

    zysk_posrd=0
    calk_koszt=0
    calk_przychod=0
    kt, tab_opt, zysk_posrd ,calk_koszt, calk_przychod =main.main_()

    return render_template("posrednik.html",
     calk_przychod=calk_przychod,
      zysk_posrd= zysk_posrd, 
      calk_koszt=calk_koszt,
      kt=kt,
      tab_opt=tab_opt)


def logistics_method():
    return "idk yet"

app.run()
