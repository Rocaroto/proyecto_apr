import random
import time
import recursos
#///////////////////////////////////////////////////////////////////////////////////// empieza el programa
inicio = time.time()
seconds1 = time.time()
t = time.localtime(seconds1)
print("El programa inicio con : ", t.tm_hour,":", t.tm_min,":",t.tm_sec) 
start=input('Escribe "empezar" para iniciar el programa')
while start == "empezar":
    print("\ncartelera del cine por categorias")

    desi = input("""\n
    //////////////////////////
    /.Que lista quieres ver?./
    /......................../
    /--comedia______|a|------/               
    /--terror_______|b|------/
    /--accion_______|c|------/
    /--aleatorio____|d|------/
    /--salir________|e|------/
    /......................../
    //////////////////////////\n""")
    #////////////////////////////////////////////////////////////////////////
    if desi =="a":
        recursos.comedia()
    #////////////////////////////////////////////////////////////////////////
    elif desi == "b":
        recursos.terror()

    #////////////////////////////////////////////////////////////////////////
    elif desi == "c":
        recursos.accion()

    #////////////////////////////////////////////////////////////////////////
    elif desi == "d":
        recursos.ma()

    #////////////////////////////////////////////////////////////////////////
    elif desi == "e":
        break
    #////////////////////////////////////////////////////////////////////////
    seconds2 = time.time()
    fin = time.localtime(seconds2)
print("el programa finaliza con: ", fin.tm_hour,"Horas :", fin.tm_min,"Minutos :",fin.tm_sec,"Segundos")
final = time.time()
print("el programa funciono por: ",final-inicio," segundos")
    