#!/bin/bash

# Définition des variables
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="/home/admin/AMS/partie2/sauvegarde/sauvegarde_${TIMESTAMP}.db"

# Création du répertoire de sauvegarde s'il n'existe pas
mkdir -p sauvegarde

# Sauvegarde de la base SQLite
cp database.db "$BACKUP_FILE"


echo "Sauvegarde effectuée : $BACKUP_FILE"
