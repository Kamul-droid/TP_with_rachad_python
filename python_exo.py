#Algorithme
# on demande à l'utilisateur de rentrer les informations

prix = int(input("Entrer le prix unitaire"))

Nombre_article=int(input("Entrer le nombre d'articles"))

TVA = float(input("Entrer la TVA"))

	
# on effectue le calcul
	
montant_ttc = (prix*Nombre_article)(1+TVA)
	
# on affiche le résultat
	
print("le montant TTC de l'achat est",montant_ttc)