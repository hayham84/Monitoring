
    <meta charset="UTF-8">
# 🖥️ Interface Web de Monitoring du Parc Informatique

## 📌 Description

Cette application permet de **visualiser en temps réel l'état des ressources système** (CPU, RAM, disque) via une interface web développée avec **Flask**.  
Les données sont affichées à la fois sous forme de **textes clairs** et de **graphique généré dynamiquement avec Pygal**.

---

## ⚙️ Fonctionnalités

- Affichage des indicateurs système :
  - Utilisation du CPU
  - Utilisation de la RAM
  - Utilisation du disque
- Génération automatique d’un graphique interactif
- Interface web avec **W3.CSS**

---

## 📂 Arborescence du projet

```
partie4/
├── page.py               # Script Flask principal
├── fichier.svg           # Graphique généré par Pygal (exemple)
├── templates/
│   └── index.html        # Template HTML principal
└── README.md             # Ce fichier
```

---

## 🧰 Prérequis

- Python 3
- Librairies Python :
  - Flask
  - Pygal
  - Psutil

---

## 🔧 Installation

1. **(Facultatif)** Créer un environnement virtuel :

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Installer les dépendances** :

   ```bash
   pip install flask pygal psutil
   ```

---

## 🚀 Exécution

Lancer le serveur Flask :

```bash
python3 page.py
```

Ensuite, accéder à l'application via votre navigateur :

- Si vous êtes en local : [http://127.0.0.1:5000](http://127.0.0.1:5000)

> ⚠️ Assurez-vous d’utiliser `host="0.0.0.0"` dans `page.run()` pour autoriser les connexions extérieures.

---

## 🎨 Exemple de rendu

- Indicateurs système affichés dans des encadrés clairs
- Graphique stylisé généré avec Pygal
- Thème W3.CSS teal intégré pour une meilleure expérience visuelle

---

## 📄 Conclusion

Cette interface permet de **surveiller l’état du système** en temps réel via une interface graphique simple et lisible.

---

## 🧠 Auteurs

Projet développé dans le cadre du module **Administration Systèmes - L2 S4 - CERI**  
Par Haytham BERHILI

