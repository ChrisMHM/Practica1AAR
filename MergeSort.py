import sys
	
def mergeSort(A, primero, ultimo):
	if primero < ultimo:
		medio = (primero + ultimo)//2
		mergeSort(A, primero, medio)
		mergeSort(A, medio+1, ultimo)
		merge(A, primero, medio, ultimo)
		
def merge(A, primero, medio, ultimo):
	L = A[primero:medio+1]
	R = A[medio+1:ultimo+1]
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