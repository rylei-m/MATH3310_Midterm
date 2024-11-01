from itertools import permutations
from sympy import isprime

years = [str(year) for year in range(1985, 1996)]

def find_prime_year_concatenation(years):
    for perm in permutations(years):
        number_str = ''.join(perm)
        number = int(number_str)
        
        if isprime(number):
            print(f"Prime found: {number}")
            return number
    
    print("No prime number found.")
    return None

find_prime_year_concatenation(years)
