#!/usr/bin/python3
# rsa_factors_advanced.py

import sys
from sympy import isprime

def pollards_rho(n):
    x, y, d = 2, 2, 1
    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_prime_factors(number):
    if isprime(number):
        return number, 1

    factor = pollards_rho(number)
    if factor is None:
        return None

    return factor, number // factor

def main(filename):
    try:
        with open(filename, 'r') as file:
            number = int(file.readline().strip())
            factors = find_prime_factors(number)
            if factors:
                print(f"{number}={factors[0]}*{factors[1]}")
            else:
                print(f"Unable to find prime factors for {number}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print(f"Invalid input in '{filename}'. Please provide a valid natural number greater than 1.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa_factors_advanced <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)

