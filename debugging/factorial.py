#!/usr/bin/env python3
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
    else:
        try:
            n = int(sys.argv[1])
            if n < 0:
                print("Please enter a non-negative integer.")
            else:
                result = factorial(n)
                print(f"The factorial of {n} is {result}")
        except ValueError:
            print("Please enter a valid integer.")
