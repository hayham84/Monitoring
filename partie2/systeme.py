#!/usr/bin/python3

import psutil
import time
import sys
#sys.path.append("/home/admin/AMS/partie2")
from data import insertion_info_systeme
import os
import subprocess

cpu = "/home/admin/AMS/partie1/sonde_cpu.py"
ram = "/home/admin/AMS/partie1/sonde_ram.sh"
disk = "/home/admin/AMS/partie1/sonde_disque.py"


def system():
    
    # Récupère le pourcentage d'usage du CPU, RAM et Disque
    try:
        # Récupérer la sortie de la commande
        cpu_usage = subprocess.run(["python3", cpu], check=True, capture_output=True, text=True)
        ram_usage = subprocess.run(["bash", ram], check=True, capture_output=True, text=True)
        disk_usage = subprocess.run(["python3", disk], check=True, capture_output=True, text=True)
        
        # Convertir la sortie en float (le pourcentage)
        cpu_usage = float(cpu_usage.stdout.strip())
        ram_usage = float(ram_usage.stdout.strip())
        disk_usage = float(disk_usage.stdout.strip())
        
        return cpu_usage, ram_usage, disk_usage
    except subprocess.CalledProcessError as e:
        print("Erreur lors de la récupération d'info :", e)

    
    
if __name__ == "__main__":
    cpu, ram, disk = system()   
    insertion_info_systeme(cpu,ram,disk)    
    print(f"Données enregistrées : CPU={cpu}% | RAM={ram}% | DISK={disk}%")
