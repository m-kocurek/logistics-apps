from scipy.optimize import linprog

print("Podaj liczbe wyrobow: ")
lw = int(input()); #np 2
obj = [0 for x in range(lw)]
print("Podaj ceny sprzedazy wyrobów: ")
for i in range(lw):
      print("wyrob %d: " %(i+1))
      obj[i] = float(input()) #np 1 i 1

print("\nPodaj liczbe surowcow: ")
ls = int(input()) #np 2

#po wprowadzeniu przykladowych liczb funkcja celu wyglada tak
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

while(True):
      print("\nOgraniczenia:")
      print("1. podaj ")
      print("2. zakończ")

      wybor = int(input())
      if (wybor == 1):

            print("\nlewa strona rownania:")
            left = [0 for x in range(lw)]
            for i in range(lw):
                  print("x%d:" % (i + 1))
                  left[i] = float(input())

            print("\nprawa strona rownania")
            right = float(input())

            print("\nznak rownania (=, <=, >=)")
            znak = input()


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

      elif (wybor == 2):
            break
      else:
            print("nie ma takiego wyboru")


for i in range(lw):
      obj[i] *= -1


opt = linprog(c=obj, A_ub=ls_eql,  b_ub=rs_eql, A_eq=ls_eq, b_eq=rs_eq, method="revised simplex")

print("\nCzy optymalizacja zakończyła się sukcesem?:   ", opt.success) #informacja czy optymalizacja przeszla pomyslnie
#print(opt.x)
print("\n")
for i in range(len(opt.x)):
      print("wyrob %d: %.2f" %(i+1,opt.x[i]))



zysk = opt.fun*(-1) #zysk koncowy

print("zysk %.2f zł" %zysk)