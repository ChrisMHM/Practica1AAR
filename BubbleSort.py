from Swap import swap

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