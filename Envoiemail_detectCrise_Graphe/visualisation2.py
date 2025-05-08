import json
import sqlite3
import pygal
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

db = "../partie2/database.db"


def argument(filename):
    with open(filename, "r") as f:
        config = json.load(f)
        return config

def generate_graph():

    # Vérification du nom de la sonde
    sondes_existant = ["cpu_usage", "ram_usage", "disk_usage"]
    #if sonde not in sondes_existant:
        #print(f"Erreur : sonde '{sonde}' non reconnue. Choisir parmi {sondes_existant}.")
        #return None

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    #query = f"SELECT timestamp, {sonde} FROM info_systeme ORDER BY timestamp"
    #cursor.execute(query)
    #data = cursor.fetchall()


    query1 = f"SELECT timestamp, cpu_usage, ram_usage, disk_usage FROM info_systeme ORDER BY timestamp"
    cursor.execute(query1)
    data = cursor.fetchall()

    conn.close()

    #timestamps = []
    #values = []
    #for row in data:
    #    timestamp_str, value = row
    #    timestamp_dt = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    #    timestamps.append(timestamp_dt.strftime("%d %H:%M:%S"))
    #    values.append(value)


    timestamps = []
    cpu = []
    ram = []
    disk = []
    for row in data:
        timestamp_str, value1, value2, value3 = row
        timestamp_dt = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        timestamps.append(timestamp_dt.strftime("%d %H:%M:%S"))
        cpu.append(value1)
        ram.append(value2)
        disk.append(value3)


    #graphe = pygal.Line(x_label_rotation=20)
    #graphe.title = f"Historique pour {sonde}"
    #graphe.x_labels = timestamps
    #graphe.add(sonde, values)


    graphe = pygal.Line(x_label_rotation=70)
    graphe.title = f"Historique des sondes"
    graphe.x_labels = timestamps
    graphe.add("CPU", cpu)
    graphe.add("RAM", ram)
    graphe.add("DISK", disk)


    graphe.render_to_file("fichier.svg") 
    print("Graphique généré !")
    chart_uri = graphe.render_data_uri()
    return chart_uri

def detecte_crise(sonde, seuil):

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = f"SELECT {sonde} FROM info_systeme ORDER BY timestamp DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    #print(result[0])

    value = result[0]
    if value > seuil:
        print(f"Situation de crise détectée pour {sonde} : valeur {value} > seuil {seuil}")
        return value,True
    else :
        return value, False

def alert_email(sujet, body, destinataire):

    msg = MIMEText(body)
    msg['Subject'] = sujet
    msg['From'] = "haytham.berhili@alumni.univ-avignon.fr"
    msg['To'] = ", ".join(destinataire)

    try:
        server = smtplib.SMTP_SSL("partage.univ-avignon.fr", 465)
        server.login("haytham.berhili@alumni.univ-avignon.fr", "Hassiaber_lebahh84000!")
        server.sendmail("haytham.berhili@alumni.univ-avignon.fr", destinataire, msg.as_string())
        server.quit()
        print("Email d'alerte envoyé avec succès.")
    except Exception as e:
        print("Erreur lors de l'envoi de l'email :", e)

def main():
    
    config = argument("argument.json")

    sonde = config["sonde"]
    seuil = config["seuil"]

    generate_graph()

    resultat_sonde,rep = detecte_crise(sonde, seuil)

    if rep == True:
        with open("mail_crise.txt", "r") as f:
            email = f.read()
            # Remplacement des placeholders dans le template
            email = email.replace("[SONDE]", sonde)
            email = email.replace("[VALEUR_ACTUELLE]", str(resultat_sonde))
            email = email.replace("[SEUIL]", str(seuil))
            email = email.replace("[DATE_HEURE]", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            destinataire = ["haytham.berhili@alumni.univ-avignon.fr"]  # Liste des destinataires 
            sujet = f"Alerte Crise : {sonde} dépasse {seuil}%"
            alert_email(sujet, email, destinataire)
    else:
        print("Aucune situation de crise détectée, aucun e-mail n'a été envoyé.")


