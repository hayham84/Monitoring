#!/bin/bash

# Fonction pour obtenir l'utilisation de la RAM en pourcentage
get_ram_usage() {
    # Extraire la mémoire totale et la mémoire utilisée
    total_mem=$(free | grep Mem | awk '{print $2}')
    usage_mem=$(free | grep Mem | awk '{print $3}')
    
    # Calculer le pourcentage d'utilisation
    ram_usage=$(( 100 * usage_mem / total_mem ))

    # Renvoie le résultat
    echo $ram_usage
}

# Exemple d'utilisation de la fonction
get_ram_usage


#echo $total_mem
#echo $usage_mem
# Calculer le pourcentage d'utilisation
#ram_usage=$(( 100 * usage_mem / total_mem ))
#return $ram_usage
#echo "Utilisation de la RAM : $ram_usage%"
#sleep 5
#done

