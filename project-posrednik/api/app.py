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


@app.route('/sieci', methods=['GET', 'POST'])
def logistics_method():
    if request.method == 'GET':
        return render_template('sieci.html')
    else:
        D_id = str(request.form['ID_d'])
        Podaz_d = str(request.form['podaz_d'])
        ID_p = str(request.form['ID_p'])
        Podaz_p = str(request.form['podaz_p'])
        ID_o = str(request.form['ID_o'])
        Popyt_o = str(request.form['popyt_o'])
        ID_polaczenia = str(request.form['ID_polaczenia'])
        koszty = str(request.form['koszty'])
        warunek = str(request.form['warunek'])

        lista_D_id=[]
        lista_D_podaz=[]
        lista_D_id.append(D_id)
        lista_D_podaz.append(Podaz_d)
        dlg_listy =len(lista_D_id)


    #pobranie danych z formularza
    # przekazanie do metody obliczeniowe
    #zwrocenie danych i wyswietlenei wyniku w tabelach
    zmienna ="abc"
    return render_template("sieci.html" ,zmienna=zmienna, lista_D_id = lista_D_id , lista_D_podaz=lista_D_podaz )

app.run()
