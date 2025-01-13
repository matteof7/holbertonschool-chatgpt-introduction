#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémente n à chaque itération
    return result

if len(sys.argv) > 1:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Veuillez entrer un nombre entier positif.")
else:
    print("Veuillez fournir un argument numérique.")
