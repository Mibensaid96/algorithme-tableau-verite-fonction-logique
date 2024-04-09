from itertools import product

def fonction_logique(a, b, c):
    # Définir votre fonction logique ici
    return (a and b) or (not b and c)

def tableau_verite(fonction):
    table_verite = []
    inputs = list(product([False, True], repeat=3))  # Génère toutes les combinaisons de 0 et 1 pour 3 variables
    
    for input_combination in inputs:
        output = fonction(*input_combination)
        table_verite.append(input_combination + (output,))
    
    return table_verite

def forme_canonique(table_verite):
    canonique = ""
    for entry in table_verite:
        if entry[-1]:  # Si la sortie est True (1)
            variables = [f'{"not " if not value else ""}x{i}' for i, value in enumerate(entry[:-1], start=1)]
            term = " and ".join(variables)
            if canonique:
                canonique += " or "
            canonique += f"({term})"
    return canonique

# Exemple d'utilisation
table_verite = tableau_verite(fonction_logique)
print("Tableau de vérité :")
for entry in table_verite:
    print(entry)

forme_canonique = forme_canonique(table_verite)
print("\nPremière forme canonique de la fonction logique :")
print(forme_canonique)
