cadena1 = []
cadena2 = []
cadena3 = []
cadenas = []

tabla = open("tabla.tex", "r")
tabla2 = open("tabla2.tex", "r")
tabla3 = open("tabla3.tex", "r")
tablaFinal = open("tablaFinal.tex", "w")

for linea in tabla:
    if linea[-1] == '\n':
        linea = linea[:-1]
    cadena1.append(linea)

for linea in tabla2:
    if linea[-1] == '\n':
        linea = linea[:-1]
    cadena2.append(linea)

for linea in tabla3:
    if linea[-1] == '\n':
        linea = linea[:-1]
    cadena3.append(linea)

cont = 0
for i in range(len(cadena1)):
    if i%2 == 0:
        cadenas.append(str(cadena1[i])+"\n")
    else:
        text = str(cadena1[i]) + str(cadena2[i]) + str(cadena3[i]) + "\n"
        cadenas.append(text)
        cont += 1

for n in cadenas:
    cadena = str(n)
    tablaFinal.write(cadena)
    cont += 100

tabla.close()
tabla2.close()
tabla3.close()
tablaFinal.close()
