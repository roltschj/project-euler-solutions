#Find the sum of all the primes below two million.

import _first_five

result = 2

for x in range(3, 2000000, 2):
    if _first_five.isPrime(x):
        result = result + x

print(result)
    
