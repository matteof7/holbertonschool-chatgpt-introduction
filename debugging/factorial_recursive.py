#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un nombre entier positif.

    Cette fonction utilise une approche récursive pour calculer
    le factoriel. Elle se rappelle elle-même avec des valeurs
    décroissantes jusqu'à atteindre le cas de base (0).

    Paramètres:
    n (int): Le nombre dont on veut calculer le factoriel.
             Doit être un entier non négatif.

    Retours:
    int: Le factoriel de n.

    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Récupère l'argument de la ligne de commande et calcule son factoriel
f = factorial(int(sys.argv[1]))
print(f)
