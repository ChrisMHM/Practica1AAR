from Swap import swap

def insercion(arreglo):
    for i in range(1, len(arreglo)):
        j = i - 1

        while j >= 0 and arreglo[j] > arreglo[j+1]:
            swap(j, j+1, arreglo)
            j = j - 1
        
    #return arreglo