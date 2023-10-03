# What is the 10001st prime number?

import _first_five

counter = 0
num = 2
prime = 2

while counter < 10001:
    if _first_five.isPrime(num):
        counter = counter + 1
        prime = num

    num += 1

print(prime) #104743
