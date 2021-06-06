from scipy.optimize import linprog
import linecache as lc
import pandas as pd

def sieci_():
     
######## ODCZYT Z PLIKU #########################

      df=pd.read_csv('baza.txt')
      dane = pd.DataFrame(data=df, columns=['A'] )

############## LICZBA WYROBOW
      Liczba_wyrobow = int(df.iat[0,0])  
      print("liczba wyrobow")
      print(Liczba_wyrobow)
      Cena_wyrobow=[0 for x in range(Liczba_wyrobow)]
                    
      lw=Liczba_wyrobow               #np 2   
      obj = [0 for x in range(lw)]

############## CENY WYROBOW
      for i in range(Liczba_wyrobow):
            Cena_wyrobow[i] = float(df.iat[1+i,0]) 
      print("ceny wyrobow")
      print(Cena_wyrobow)
         
      for i in range(lw):
            obj[i] = Cena_wyrobow[i]   #np 1 i 1

############# LICZBA SUROWCOW 
      Liczba_surowcow = int(df.iat[Liczba_wyrobow+1,0]) 
      print("liczba surowcow")
      print(Liczba_surowcow)
             
      ls=Liczba_surowcow                  #np 2

############ LICZBA OGRANICZEN 
      Liczba_Ograniczen= int (df.iat[Liczba_wyrobow +2,0]) 
      print("liczba ograniczen")
      print(Liczba_Ograniczen)

#petla for do  pobrania i podzielenia rownania
      for i in range(Liczba_Ograniczen):
            Ograniczenia=df.iat[Liczba_wyrobow+3+i,0]
            split_tab_ogr=Ograniczenia.split(':')
            print("znak")
            print(split_tab_ogr[-2])
            print("prawa strona rownania") 
            print(split_tab_ogr[-1])
            print("same wspolczynniki!") 
            print(split_tab_ogr[:-2]) #wyszly tylko wspolczynniki bez znaku i PRAWEJ strony rownania
      
      open("baza.txt", "w").close() #wyczysc plik
      open("baza.txt", "w").write(". \n") #wrzuc krope i dawaj dalej XD

###############################################
#po wprowadzeniu przykladowych 
# liczb funkcja celu wyglada tak:
#funkcja celu
# z = x1 + x2 -> max
#wartosci domyslne, w przypadku gdy uzytkownik nie poda ograniczen
#dla ograniczenia <=
      ls_eql = [[0 for x in range(lw)]]#lew strona ograniczen <=
      rs_eql = [0] #prawa strona oograniczen <=
#dla ograniczenia >=, wszystko należy przemnożyć przez -1
#dla ograniczenia =
      ls_eq = [[0 for x in range(lw)]]
      rs_eq = [0]
#przykladowe ograniczenia
# 6x1+6x2 <= 36000
# 10x1 + 5x2 <= 50000
# x2 <= 4000

      for i in range(Liczba_Ograniczen):
            Ograniczenia=df.iat[Liczba_wyrobow+3+i,0]
            split_tab_ogr=Ograniczenia.split(':')
            print("znak")
            print(split_tab_ogr[-2])
            znak= split_tab_ogr[-2]

            print("prawa strona rownania") 
            print(split_tab_ogr[-1])
            right= float(split_tab_ogr[-1] )

            print("\nlewa strona rownania:")
            print(split_tab_ogr[:-2]) 
            left = [0 for x in range(lw)]
            wspolczynniki = split_tab_ogr[:-2]
            for i in range(lw): 
                  left[i] = wspolczynniki[i]

            #print("\nznak rownania (=, <=, >=)") 
            if (znak == "="):
                  ls_eq.append([x for x in left])
                  rs_eq.append(right)
            elif (znak == "<="):
                  ls_eql.append([x for x in left])
                  rs_eql.append(right)
            elif (znak == ">="):
                  ls_eql.append([x * (-1) for x in left])
                  rs_eql.append(right * (-1))
            else:
                  print("nie ma takiego znaku do wyboru")

      for i in range(lw):
            obj[i] *= -1

      opt = linprog(c=obj, A_ub=ls_eql,  b_ub=rs_eql, A_eq=ls_eq, b_eq=rs_eq, method="revised simplex")

      print("\nCzy optymalizacja zakończyła się sukcesem?:   ", opt.success) #informacja czy optymalizacja przeszla pomyslnie
      print(opt.x)

      zysk = opt.fun*(-1) #zysk koncowy
      wynik = opt.success
      wspolczynniki = opt.x

      print("zysk %.2f zł" %zysk)
      return zysk, wynik, wspolczynniki
