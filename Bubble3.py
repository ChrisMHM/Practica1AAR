#Algoritmo practica

def swap(j, i, arreglo):
    aux = arreglo[i]
    arreglo[i] = arreglo[j]
    arreglo[j] = aux

def bubble(A):
    n = len(A)
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(n-1):
            if A[i] > A[i+1]:
                swap(i, i+1, A)
                swapped = True
        n = n - 1

        if not swapped:
            break

    return A

arreglo = [5, 2, 4, 6, 1, 3, 3, 9, 10, 7, 8, 1]
nuevoArreglo = bubble(arreglo)
print(nuevoArreglo)