import random
import time

a=["super cool","ted","la fiesta de las salchichas","cazafantasmas"]
b=["get out","la bruja","insidious","bird box: a ciegas"]
c=["john wick","la vieja guardia","lucy"]

#///////////////////////////////////////////////////////////////////////////////////// se crea las funciones de las listas
def comedia():
    print("Peliculas de comedia:\n")
    for ax in a:
        print(ax)
    print("\naqui hay ",len(a)," peliculas\n")
    
    n1= input("""
    deseas hacer algo con la lista?  si - no
    \n""")
    while n1 == "si":
        an1 =input("""\n
    saber la posicion = |1|
    agregar pelicula  = |2|
    eliminar pelicula = |3|
    regresar          = |4|
    mostrar lista     = |5|
        \n""")
        if an1 == "1":
            lin=input("de la lista, cual posicion deseas saber?\n")
            if lin in a:
                print("\n",lin," esta en la posicion: ",a.index(lin))
            else:
                print("\ndebiste escribir algo de la lista\n")
                
        elif an1 == "2":
            lin2=input("que pelicula quieres agregar? ")
            if lin2 in a:
                print("la pelicula ya esta ahi")
            else:
                a.append(lin2)
                print("se agrego: ",lin2," a la lista")
            
        elif an1 == "3":
            lin3=input("que pelicula de la lista quieres eliminar?")
            if lin3 in a:
                a.remove(lin3)
                print("se removio: ",lin3," de la lista")
            else:
                print("la pelicula tiene que estar en la lista")
        elif an1 =="4":
            break
            
        elif an1 == "5":
            for cx in a:
                print(cx)
        else:
            print("ingresa un valor valido")

def terror():
    print("Peliculas De Terror:\n")
    for bx in b:
        print(bx)
    print("\naqui hay ",len(b)," peliculas")
    n2= input("""
    deseas hacer algo con la lista?  si - no
    \n""")
    while n2 == "si":
        an1 =input("""\n
    saber la posicion = |1|
    agregar pelicula  = |2|
    eliminar pelicula = |3|
    regresar          = |4|
    mostrar lista     = |5|
        \n""")
        if an1 == "1":
            lin=input("de la lista, cual posicion deseas saber?\n")
            if lin in b:
                print("\n",lin," esta en la posicion: ",b.index(lin))
            else:
                print("\ndebiste escribir algo de la lista\n")
                
        elif an1 == "2":
            lin2=input("que pelicula quieres agregar? ")
            if lin2 in b:
                print("la pelicula ya esta ahi")
            else:
                b.append(lin2)
                print("se agrego: ",lin2," a la lista")
            
        elif an1 == "3":
            lin3=input("que pelicula de la lista quieres eliminar?")
            if lin3 in b:
                b.remove(lin3)
                print("se removio: ",lin3," de la lista")
            else:
                print("la pelicula tiene que estar en la lista")
        elif an1 =="4":
            break
            
        elif an1 == "5":
            for cx in b:
                print(cx)
        else:
            print("ingresa un valor valido")
            
def accion():
    print("Peliculas De Accion:\n")
    for cx in c:
        print(cx) 
    print("\naqui hay ",len(c)," peliculas")
    n3= input("""
    deseas hacer algo con la lista?  si - no
    \n""")
    while n3 == "si":
        an1 =input("""\n
    saber la posicion = |1|
    agregar pelicula  = |2|
    eliminar pelicula = |3|
    regresar          = |4|
    mostrar lista     = |5|
        \n""")
        if an1 == "1":
            lin=input("de la lista, cual posicion deseas saber?\n")
            if lin in c:
                print("\n",lin," esta en la posicion: ",c.index(lin))
            else:
                print("\ndebiste escribir algo de la lista\n")
                
        elif an1 == "2":
            lin2=input("que pelicula quieres agregar? ")
            if lin2 in c:
                print("la pelicula ya esta ahi")
            else:
                c.append(lin2)
                print("se agrego: ",lin2," a la lista")
            
        elif an1 == "3":
            lin3=input("que pelicula de la lista quieres eliminar?")
            if lin3 in c:
                c.remove(lin3)
                print("se removio: ",lin3," de la lista")
            else:
                print("la pelicula tiene que estar en la lista")
        elif an1 =="4":
            break
            
        elif an1 == "5":
            for cx in c:
                print(cx)
        else:
            print("ingresa un valor valido")
def ma():
  def comedia1():
     comedia()
  def terror1():
     terror()
  def accion1():
     accion()
  def run():
     ei = random.choice([comedia1,terror1,accion1])
     ei()
  run()