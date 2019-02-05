from InsertionSort import *
from QuickSort import *
from MergeSort import *
from BubbleSort import *
import time
import sys
import shutil
import os

def listasTiempoEjecucion(tiempoEjecucion, tiemposInsert ,tiemposMerge ,tiemposBubble ,tiemposQuick):
    tiemposInsert.append(tiempoEjecucion[0])
    tiemposMerge.append(tiempoEjecucion[1])
    tiemposBubble.append(tiempoEjecucion[2])
    tiemposQuick.append(tiempoEjecucion[3])


def ejecucion(elementos):
    sys.setrecursionlimit(20000)
    file = open("/home/christian/Documentos/Github/Practica1AAR/Descendentes/descendentes_"+ str(elementos) +".txt", "r")
    arreglo1 = []
    arreglo2 = []
    arreglo3 = []
    arreglo4 = []
    tiempoEjecucion = []

    for linea in file.readlines():
        if linea[-1] == '\n':
            linea = linea[:-1]
        arreglo1.append(int(linea))
        arreglo2.append(int(linea))
        arreglo3.append(int(linea))
        arreglo4.append(int(linea))

    file.close()

    #################################################
    inicio = time.time()
    insercion(arreglo1)
    fin = time.time()
    tiempoEjecucion.append(float("{0:.4f}".format(fin - inicio)))
    #################################################
    inicio = time.time()
    mergeSort(arreglo3, 0, len(arreglo3)-1)
    fin = time.time()
    tiempoEjecucion.append(float("{0:.4f}".format(fin - inicio)))
    #################################################
    inicio = time.time()
    bubble(arreglo2)
    fin = time.time()
    tiempoEjecucion.append(float("{0:.4f}".format(fin - inicio)))
    #################################################
    inicio = time.time()
    quickSort(arreglo4, 0, len(arreglo4)-1)
    fin = time.time()
    tiempoEjecucion.append(float("{0:.4f}".format(fin - inicio)))
    #################################################

    return tiempoEjecucion

def escribeArchivo(file, lista):
    cont = 100
    f = open (file, "w")
    for e in lista:
        cadena = str(cont) + " " + str(e) + "\n"
        f.write(cadena)
        cont += 100
    f.close()

def escribeArchivoLatex(archivo, insert, merge, bubble, quick):
    cont = 100
    file = open(archivo, "w")
    for n in range(len(insert)):
        file.write("\\hline\n")
        cadena = str(cont) + " & " + str(insert[n]) + " & " + str(merge[n]) + " & " + str(bubble[n])  + " & " + str(quick[n]) + " &\\\\\n"
        file.write(cadena)
        cont += 100
        
    file.write("\\hline")
    file.close()

def move(src, filename, dest):
    shutil.move(os.path.join(src, filename), os.path.join(dest, filename))

def main():
    total = 2000
    n = 100
    cont = 0
    
    tiempoEjecucicon = []

    tiemposInsert = []
    tiemposMerge = []
    tiemposBubble = []
    tiemposQuick = []

    archivoInsert = "archivoDescInsert.txt"
    archivoMerge = "archivoDescMerge.txt"
    archivoBubble = "archivoDescBubble.txt"
    archivoQuick = "archivoDescQuick.txt"
    archivoLatex = "tabla.tex"

    while n <= total:
        tiempoEjecucicon = ejecucion(n)
        listasTiempoEjecucion(tiempoEjecucicon, tiemposInsert, tiemposMerge, tiemposBubble, tiemposQuick)
        n += 100
        cont += 1

    escribeArchivoLatex(archivoLatex, tiemposInsert, tiemposMerge, tiemposBubble, tiemposQuick)

    escribeArchivo(archivoInsert, tiemposInsert)
    escribeArchivo(archivoMerge, tiemposMerge)
    escribeArchivo(archivoBubble, tiemposBubble)
    escribeArchivo(archivoQuick, tiemposQuick)

    move("/home/christian/Documentos/Github/Practica1AAR", "archivoDescInsert.txt", "/home/christian/Documentos/Github/Practica1AAR/GraficaDesc")
    move("/home/christian/Documentos/Github/Practica1AAR", "archivoDescMerge.txt", "/home/christian/Documentos/Github/Practica1AAR/GraficaDesc")
    move("/home/christian/Documentos/Github/Practica1AAR", "archivoDescBubble.txt", "/home/christian/Documentos/Github/Practica1AAR/GraficaDesc")
    move("/home/christian/Documentos/Github/Practica1AAR", "archivoDescQuick.txt", "/home/christian/Documentos/Github/Practica1AAR/GraficaDesc")

    #for i in range(cont):
    #    print(i, tiemposInsert[i], tiemposMerge[i], tiemposBubble[i], tiemposQuick[i])

    print("Numero de ejecuciones: " + str(cont))

if __name__ == "__main__":
    main()