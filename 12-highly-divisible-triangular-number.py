#What is the value of the first triangle number to have over
#five hundred divisors?

import math

def getNumFactors(num):

    factors = 0

    for i in range(1, math.ceil(math.sqrt(num))):
        if num % i == 0:
            factors = factors + 2
            if i * i == num:
                    factors = factors - 1

    return factors

n = 1

numDivisors = 0

while numDivisors < 501:
    if n % 2 == 0:
        numDivisors = getNumFactors(n / 2) * getNumFactors(n + 1)
    else:
        numDivisors = getNumFactors(n) * getNumFactors((n + 1) / 2)

    n = n + 1

result = int(((n - 1) / 2) * n)

print(str(result) + " has " + str(numDivisors) + " divisors.")
