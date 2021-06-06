import flask as Flask
from flask import *
from flask import session
import sieci
from sieci import sieci_
import flask
from flask import Flask,request, jsonify, render_template, redirect, url_for, session
import sys
import os

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

    return render_template("posrednik.html",
     calk_przychod=calk_przychod,
     zysk_posrd= zysk_posrd, 
      calk_koszt=calk_koszt,
      kt=kt,
      tab_opt=tab_opt )


@app.route('/sieci', methods=['GET', 'POST'])
def sieci():
    if request.method == 'GET':
        return render_template('sieci.html')
    else:

        liczba_wyrobow = str(request.form['liczba_wyrobow'])
        session['liczba_wyrobow'] = liczba_wyrobow
        if(liczba_wyrobow != 0):
           with open('baza.txt', 'a') as plik:
                plik.write(liczba_wyrobow)
                plik.write("\n")
               # plik.close()

        cena = str(request.form['wyrob_cena'])
        if(cena !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(cena)
                plik.write("\n")
               # plik.close() 
       
        liczba_surowcow = str(request.form['liczba_surowcow'])
        if(liczba_surowcow !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(liczba_surowcow)
                plik.write("\n")
               # plik.close() 
        session['liczba_surowcow']=liczba_surowcow

        liczba_ograniczen = str(request.form['liczba_ograniczen'])
        if(liczba_ograniczen !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(liczba_ograniczen)
                plik.write("\n")
               # plik.close() 
       

        x1 = str(request.form['x1'])
        if(x1 !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(x1)
                plik.write("\t")
                plik.close() 

        x2 = str(request.form['x2'])
        if(x2 !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(x2)
                plik.write("\t")
                plik.close() 
        x3 = str(request.form['x3'])
        if(x3 !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(x3)
                plik.write("\t")
                plik.close() 
        x4 = str(request.form['x4'])
        if(x4 !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(x4)
                plik.write("\t")
                plik.close() 
        znka = str(request.form['znak'])
        if(znka !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(znka)
                plik.write("\t")
                plik.close() 
        pr_strona = str(request.form['pr_strona'])
        if(pr_strona !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(pr_strona)
                plik.write("\t")
                plik.close() 
                   
       # with open('baza.txt', 'a') as plik:
            #for linia in plik:
             #print (linia.strip().split())

        #plik = open('baza.txt','w')
       #    plik.write(liczba_wyrobow)
        #   plik.write("\n")
      #  plik.close()

       # dlg_listy =len(lista_D_id)
    zmienna ="abc"
    return render_template("sieci.html", zmienna=zmienna)

######### LICZBA WYROBOW

@app.route('/wpiszLW', methods=['GET','POST'])
def wpiszLW():
    if request.method == 'GET':
        zmienna="Wpisz liczbe wyrobow"
        return render_template('wpiszLW.html',zmienna=zmienna)
    else:    
        liczba_wyrobow = str(request.form['liczba'])
        session['liczba_wyrobow'] = liczba_wyrobow
        if(liczba_wyrobow != 0):
           with open('baza.txt', 'a') as plik:
                plik.write(liczba_wyrobow)
                plik.write("\n")
               # plik.close()
                 
    zmienna="wpisz liczbe wyrobow"
    return render_template("wpiszLW.html", zmienna=zmienna)

#CENA WYROBOW
@app.route('/wpiszCW', methods=['GET','POST'])
def wpiszCW():
    if request.method == 'GET':
        zmienna="Wpisz cenę wyrobów"
        return render_template('wpiszCW.html', zmienna=zmienna)
    else:    
        cena = str(request.form['liczba'])
        if(cena !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(cena)
                plik.write("\n")
               # plik.close() 
    zmienna="Wpisz cenę wyrobów"
    return render_template("wpiszCW.html", zmienna=zmienna)

#LICZBA SUROWCOW
@app.route('/wpiszLS', methods=['GET','POST'])
def wpiszLS():
    if request.method == 'GET':
        zmienna="Wpisz liczbę surowców " 
        return render_template('wpiszLS.html', zmienna=zmienna)
    else:    
        cena = str(request.form['liczba'])
        if(cena !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(cena)
                plik.write("\n")
               # plik.close() 
                 
    zmienna="Wpisz liczbę surowców " 
    return render_template("wpiszLS.html", zmienna=zmienna)

#wpisz LICZBE OGRANICZEN 
@app.route('/wpiszLOgr', methods=['GET','POST'])
def wpiszLOgr():
    if request.method == 'GET':
        zmienna="Wpisz liczbę ograniczeń" 
        return render_template('wpiszLOgr.html')
    else:
        cena = str(request.form['liczba'])
        if(cena !=0):
            with open('baza.txt', 'a') as plik:
                plik.write(cena)
                plik.write("\n")
               # plik.close() 
                 
    zmienna="Wpisz liczbę ograniczeń " 
    return render_template("wpiszLOgr.html", zmienna=zmienna)


################################## new method
#wpisz ograniczenia
@app.route('/wpiszOgraniczenie', methods=['GET','POST'])
def wpiszOgraniczenie():
    df=pd.read_csv('baza.txt')
    dane = pd.DataFrame(data=df, columns=['A'] )
    Liczba_wyrobow = int(df.iat[0,0])  
    print(Liczba_wyrobow)
    if request.method == 'GET':
        if(Liczba_wyrobow == 1):
            return render_template('wpisz_ogr-1.html')
        elif(Liczba_wyrobow == 2):
            return render_template('wpisz_ogr-2.html')
        elif(Liczba_wyrobow == 3):
            return render_template('wpisz_ogr-3.html')
        elif(Liczba_wyrobow == 4):
            return render_template('wpisz_ogr-4.html')
        
    else:
        if(Liczba_wyrobow == 1):
           x1 = str(request.form['x1'])
           if(x1 !=0):
             with open('baza.txt', 'a') as plik:
                plik.write(x1)
                plik.write(":")
                plik.close() 

           znka = str(request.form['znak'])
           if(znka !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(znka)
                    plik.write(":")
                    plik.close() 

           pr_strona = str(request.form['pr_strona'])
           if(pr_strona !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(pr_strona)
                    plik.write("\n")
                    plik.close() 

        elif(Liczba_wyrobow == 2):
            x1 = str(request.form['x1'])
            if(x1 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x1)
                    plik.write(":")
                    plik.close() 

            x2 = str(request.form['x2'])
            if(x2 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x2)
                    plik.write(":")
                    plik.close()

            znka = str(request.form['znak'])
            if(znka !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(znka)
                    plik.write(":")
                    plik.close() 
            pr_strona = str(request.form['pr_strona'])
            if(pr_strona !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(pr_strona)
                    plik.write("\n")
                    plik.close() 

        elif(Liczba_wyrobow == 3):
            x1 = str(request.form['x1'])
            if(x1 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x1)
                    plik.write(":")
                    plik.close() 

            x2 = str(request.form['x2'])
            if(x2 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x2)
                    plik.write(":")
                    plik.close() 
            x3 = str(request.form['x3'])
            if(x3 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x3)
                    plik.write(":")
                    plik.close() 

            znka = str(request.form['znak'])
            if(znka !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(znka)
                    plik.write(":")
                    plik.close() 
            pr_strona = str(request.form['pr_strona'])
            if(pr_strona !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(pr_strona)
                    plik.write("\n")
                    plik.close() 

        elif(Liczba_wyrobow == 4):
            
            x1 = str(request.form['x1'])
            if(x1 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x1)
                    plik.write(":")
                    plik.close() 

            x2 = str(request.form['x2'])
            if(x2 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x2)
                    plik.write(":")
                    plik.close() 
            x3 = str(request.form['x3'])
            if(x3 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x3)
                    plik.write(":")
                    plik.close() 
            x4 = str(request.form['x4'])
            if(x4 !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(x4)
                    plik.write(":")
                    plik.close() 

            znka = str(request.form['znak'])
            if(znka !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(znka)
                    plik.write(":")
                    plik.close() 

            pr_strona = str(request.form['pr_strona'])
            if(pr_strona !=0):
                with open('baza.txt', 'a') as plik:
                    plik.write(pr_strona)
                    plik.write("\n")
                    plik.close() 

    if(Liczba_wyrobow == 1):
        return render_template('wpisz_ogr-1.html')
    elif(Liczba_wyrobow == 2):
        return render_template('wpisz_ogr-2.html')
    elif(Liczba_wyrobow == 3):
        return render_template('wpisz_ogr-3.html')
    elif(Liczba_wyrobow == 4):
        return render_template('wpisz_ogr-4.html')



#############################################################################

@app.route('/sieci-wyniki', methods=['GET'])
def PokazWyniki():
    zysk, wynik_opt, wspolczynniki = sieci_()

    #wspolczynniki =  wspol[0] 
    return render_template("wyniki.html", zysk=zysk, wynik_opt=wynik_opt , wspolczynniki=wspolczynniki)
    
app.secret_key = " tr3yg4iwyhbfskcb74yir3hufw"
app.run()

