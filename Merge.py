
#---------------------------------------
# Merge Sort
#---------------------------------------
import sys
	
def mergeSort(A, primero, ultimo):
	if primero < ultimo:
		medio = (primero + ultimo)//2
		mergeSort(A, primero, medio)
		mergeSort(A, medio+1, ultimo)
		merge(A, primero, medio, ultimo)
	
	return A
		
def merge(A, primero, medio, ultimo):
	L = A[primero:medio]
	R = A[medio:ultimo+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i = j = 0
	
	for k in range (primero, ultimo+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
nuevoA = mergeSort(A, 0, len(A)-1)
print(nuevoA)