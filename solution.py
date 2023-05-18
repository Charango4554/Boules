# Liste des boules disponibles
boules = [1, 3, 5, 7, 9, 11, 13, 15]

# Fonction pour trouver les combinaisons possibles
def trouver_combinaison():
    for i in range(len(boules)):
        for j in range(i+1, len(boules)):
            for k in range(j+1, len(boules)):
                if boules[i] + boules[j] + boules[k] == 30:
                    return [boules[i], boules[j], boules[k]]
    return None

# Appel de la fonction pour trouver la combinaison
combinaison = trouver_combinaison()

# Vérification du résultat
if combinaison is not None:
    print("La combinaison est :", combinaison)
else:
    print("Aucune combinaison.")
