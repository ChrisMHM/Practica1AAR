def swap(j, i, arreglo):
    aux = arreglo[i]
    arreglo[i] = arreglo[j]
    arreglo[j] = aux

def insercion(arreglo):
    for i in range(1, len(arreglo)):
        valor = arreglo[i]
        j = i - 1

        while j >= 0 and arreglo[j] > arreglo[j+1]:
            swap(j, j+1, arreglo)
            j = j - 1
        
    return arreglo

arreglo = [5, 2, 4, 6, 1, 3, 3, 9, 10, 7, 8, 1]
nuevoArreglo = insercion(arreglo)
print(nuevoArreglo)