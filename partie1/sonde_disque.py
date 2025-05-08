#!/bin/bash/python


import psutil
import time


def disque():
    disque = psutil.disk_usage('/').percent
    return disque

d = disque()

print(d)

#time.sleep(5)


