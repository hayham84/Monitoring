#!/bin/bash/py

import psutil
import time

def info_cpu():
    #on prend le pourcentage utiliser du cpu sur 1 seconde
    cpu = psutil.cpu_percent(interval=1)
    #on prend la valeur de la ram qu'on met en pourcentage
    #ram = psutil.virtual_memory().percent

    #print("Usage du CPU : ", cpu)
    return cpu
    #print("Usage de la RAM :",ram)


i = info_cpu()
print(i)
#time.sleep(5)


