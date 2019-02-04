def swap(j, i, arreglo):
    aux = arreglo[i]
    arreglo[i] = arreglo[j]
    arreglo[j] = aux
	
def quickSort(A, izquierda, derecha):
    if izquierda < derecha:
        p = particion(A, izquierda, derecha)
        quickSort(A, izquierda, p - 1)
        quickSort(A, p + 1, derecha)
    return A
	
def getPivote(A, izquierda, derecha):
    medio = (derecha + izquierda) // 2
    pivote = derecha

    if A[izquierda] < A[medio]:
        if A[medio] < A[derecha]:
            pivote = medio
            
    elif A[izquierda] < A[derecha]:
        pivote = izquierda
        
    return pivote
	

def particion(A, izquierda, derecha):
    indicePivote = getPivote(A, izquierda, derecha)
    pivoteValue = A[indicePivote]
    swap(indicePivote, izquierda, A)
    borde = izquierda
    
    for i in range(izquierda, derecha+1):
        if A[i] < pivoteValue:
            borde += 1
            swap(i, borde, A)
	
    swap(izquierda, borde, A)
    
    return (borde)
	
A = [5,9,1,2,4,8,6,3,7]
print(A)
nuevoA = quickSort(A, 0, len(A)-1)
print(A)