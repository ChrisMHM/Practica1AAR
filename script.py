import os
import sys

n = (int)(sys.argv[1])

if n%100==0:
    cmd = "python3 EjecucionAsc.py " + str(n)
    os.system(cmd)
    cmd = "python3 EjecucionDesc.py " + str(n)
    os.system(cmd)
    cmd = "python3 EjecucionProm.py " + str(n)
    os.system(cmd)
    cmd = "python3 UnirTablas.py"
    os.system(cmd)
else:
    print("Error")