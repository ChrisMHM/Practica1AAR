def escribeArchivo(archivo, insert, merge, bubble, quick):
    file = open(archivo, "w")
    for n in range(len(insert)):
        file.write("\\hline")
        cadena = str((n+1)*100) + " & " + insert[n] + merge[n+1] + " & " + bubble  + " & " + quick[n]  + " &\\\\\n"
        file.write(cadena)
    
    file.write("\\hline")