import matplotlib.pyplot as plt

archivos = [
    'archivoDescInsert.txt', 'archivoDescMerge.txt', 'archivoDescBubble.txt',
    'archivoDescQuick.txt'
]
color = ['blue', 'red', 'green', 'yellow']
nombreLinea = ['Insert Sort', 'Merge Sort', 'Bubble Sort', 'Quicksort']


i = 0
for a in archivos:
    X, Y = [], []

    for line in open(a, 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])
    plt.plot(X, Y, color=color[i], label = nombreLinea[i])
    i = i +1


plt.legend(loc='upper left')
plt.title("Peor Caso")
plt.xlabel("Tamanio del arreglo")
plt.ylabel("Tiempo en segundos")
plt.grid()
plt.show()
