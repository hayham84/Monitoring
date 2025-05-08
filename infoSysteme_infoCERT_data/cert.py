#!/usr/bin/env python3
import requests
import sqlite3
import time
from bs4 import BeautifulSoup
from data import insertion_cert_alerte

CERT_URL = "http://www.cert.ssi.gouv.fr/"

def derniere_alerte():
    pageHtml = requests.get(CERT_URL) #telecharge la page html
    if pageHtml.status_code == 200: #200 correpsond a OK en HTTP
        soup = BeautifulSoup(pageHtml.text, 'html.parser') #rend la page navigable
        alerte = soup.find('div', {'class': 'item-title'})  # Sélection de la dernière alert
        print(alerte)
        a = alerte.find('a')
        print('a =', a)
        titre = a.text.strip()
        print('titre = ', titre)
        lien = 'http://www.cert.ssi.gouv.fr' + a['href']
        print(lien )
        return titre, lien
    return None, None


titre, lien = derniere_alerte()
if titre and lien:
    insertion_cert_alerte(titre, lien)
    print("Alerte CERT enregistrée :", titre ,lien)
    #time.sleep(30)  # Attendre 300 secondes (5 minutes)
