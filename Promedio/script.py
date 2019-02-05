import os


n = 100
cont = 0

while n <= 10000:
    cmd = "python aleatorios.py " + str(n) + " 0 10000"
    os.system(cmd)
    n = n + 100
    cont = cont + 1

print("numero de archivos: " + str(cont))
