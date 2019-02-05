import sys

def peorCaso(n):
    lista = []
    for i in range(n, 0, -1):
        lista.append(i)
    return lista

def escribeArchivo(file, lista):
    f = open (file, "w")
    for e in lista:
        f.write("%d\n" % e)

    f.close()

def main():
    elementos = (int)(sys.argv[1])
    lista = peorCaso(elementos)
    nameFile = "descendentes_" + str(elementos) + ".txt"
    escribeArchivo(nameFile, lista)

if __name__== "__main__":
    main()