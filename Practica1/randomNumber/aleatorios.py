import random
import sys

def creaAleatorios(n, min, max):
    lista  = []
    for i in range(0, n):
        lista.append(random.randint(min, max))
    return lista

def escribeArchivo(file, lista):
    f = open (file, "w")
    for e in lista:
        f.write("%d\n" % e)

    f.close()


if len(sys.argv) != 4:
    print("Execute python aleatorios.py [numero de elementos] [rango minimo] [rango maximo]")
else:
    elementos = (int)(sys.argv[1])
    min = (int)(sys.argv[2])
    max = (int)(sys.argv[3])
    lista = creaAleatorios(elementos, min, max)
    nameFile = "random_" + str(elementos) + ".txt"
    escribeArchivo(nameFile, lista)


