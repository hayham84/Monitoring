#!/usr/bin/env python3


import sqlite3
import os
import time
from datetime import datetime, timedelta, UTC


DB_FILE = "/home/admin/AMS/partie2/database.db"

def creation_table():
    
    #Connexion avec la bdd
    conn = sqlite3.connect(DB_FILE)
    query = conn.cursor()


    #Table pour stocker les informations système
    query.execute("""
    CREATE TABLE IF NOT EXISTS info_systeme (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        cpu_usage REAL,
        ram_usage REAL,
        disk_usage REAL
    )
    """)
    
    #Table pour stocker les alertes CERT
    query.execute("""
    CREATE TABLE IF NOT EXISTS alertes_cert (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        titre TEXT,
        lien TEXT
        )
    """)

    conn.commit()
    conn.close()

#Insère les données système dans la base SQLite
def insertion_info_systeme(cpu, ram, disk):
    conn = sqlite3.connect(DB_FILE)
    query = conn.cursor()
    temps_sec = int(time.time())
    date = datetime.utcfromtimestamp(temps_sec).strftime('%Y-%m-%d %H:%M:%S')
    query.execute("INSERT INTO info_systeme (timestamp, cpu_usage, ram_usage, disk_usage) VALUES (?, ?, ?, ?)",
                (date, cpu, ram, disk))
    conn.commit()
    conn.close()

#Insère une alerte CERT dans la base SQLite.
def insertion_cert_alerte(titre, lien):
    conn = sqlite3.connect(DB_FILE)
    query = conn.cursor()
    temps_sec = int(time.time())
    date = datetime.utcfromtimestamp(temps_sec).strftime('%Y-%m-%d %H:%M:%S')
    query.execute("INSERT INTO alertes_cert (timestamp, titre, lien) VALUES (?, ?, ?)",
                (date, titre, lien))
    conn.commit()
    conn.close()

def suppression_donnee_anciennes(delai_jours):
    """
    Supprime les données trop anciennes des tables info_systeme et alertes_cert.
    
    """
    # Connexion à la base de données
    conn = sqlite3.connect(DB_FILE)
    query = conn.cursor()

    # Calcul du timestamp limite
    #Calcule la date limite en soustrayant delai_jours à la date actuelle.
    #On compare ensuite cette date avec celles stockées en base de données.
    date_actuelle = datetime.now(UTC)
    date_limite = date_actuelle - timedelta(days=delai_jours)

    # Suppression dans info_systeme
    query.execute("SELECT id, timestamp FROM info_systeme")
    for row in query.fetchall():
        id_entry, timestamp = row
        try:
            timestamp_date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')  # Convertir le texte en date
            timestamp_date = timestamp_date.replace(tzinfo=UTC)
            if timestamp_date < date_limite:  # Comparaison
                query.execute("DELETE FROM info_systeme WHERE id = ?", (id_entry,))
        except ValueError:
            print(f"Erreur de format pour l'entrée {id_entry} : {timestamp_str}")

    
    # Suppression dans alertes_cert
    query.execute("SELECT id, timestamp FROM alertes_cert")
    for row in query.fetchall():
        id_entry, timestamp = row
        try:
            timestamp_date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            timestamp_date = timestamp_date.replace(tzinfo=UTC)
            if timestamp_date < date_limite:
                query.execute("DELETE FROM alertes_cert WHERE id = ?", (id_entry,))
        except ValueError:
            print(f"Erreur de format pour l'entrée {id_entry} : {timestamp_str}")

    # Validation des suppressions
    conn.commit()
    conn.close()

    print(f"Suppression des données antérieures au {date_limite.strftime('%Y-%m-%d %H:%M:%S')} effectuée.")


# Calcul du timestamp limite
#date_actuelle = datetime.utcnow()
#date_limite = date_actuelle - timedelta(30)
#print(date_actuelle)
#print(date_limite)
#print(timedelta(30))
#suppression_donnee_anciennes(5)
#Creation des tables
#creation_table()
