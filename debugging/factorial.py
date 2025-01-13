#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Le facteuriel n'est pas défini pour les nombres négatifs.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Veuillez fournir exactement un argument.")
        
        # Convertir l'argument en entier
        number = int(sys.argv[1])
        
        # Calculer le factoriel
        f = factorial(number)
        print(f"Le factoriel de {number} est {f}")
    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")
