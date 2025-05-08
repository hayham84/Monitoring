#!/bin/bash

# Chemin de la sauvegarde à restaurer (dernier fichier enregistré)
BACKUP_FILE=$(find /home/admin/AMS/partie2/sauvegarde -name 'sauvegarde*.db' | sort | tail -n 1)

if [ -f "$BACKUP_FILE" ]; then
    cp "$BACKUP_FILE" "/home/admin/AMS/partie2/database.db"
    echo "Base de données restaurée depuis : $BACKUP_FILE"
else
    echo "Aucune sauvegarde trouvée !"
fi

