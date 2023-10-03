# First 100 problems in Project Euler
# Author: James Roltsch

import math

# 1: Find the sum of all the multiples of 3 or 5 below 1000.

def addMultiplesOfThreeOrFive(num):

    sum = 0
    
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print(sum)

#addMultiplesOfThreeOrFive(1000) #233168

# 2: By considering the terms in the Fibonacci sequence whose values do not
#    exceed four million, find the sum of the even-valued terms.

def sumEvenFibNums(num):

    fibNum1 = 0
    fibNum2 = 1

    sum = 0

    while fibNum1 + fibNum2 < num:
        workingFibNum = fibNum1 + fibNum2

        if workingFibNum % 2 == 0:
            sum += workingFibNum

        fibNum1 = fibNum2
        fibNum2 = workingFibNum

    print(sum) 

#sumEvenFibNums(4000000) #4613732

# 3: What is the largest prime factor of the number 600851475143?

def isPrime(num):

    i = 2

    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1

    return True

def collectPrimeFactors(num):

    primeFactors = []

    i = 2

    while i <= num:
        if (isPrime(i) and num % i == 0):
            primeFactors.append(i)
            num = num / i
        i += 1

    print(primeFactors)

#collectPrimeFactors(600851475143) #[71, 839, 1471, 6857] (answer: 6857)

# 4: Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):

    sNum = str(num)
    i = 0
    j = len(sNum) - 1

    while i <= j:
        if sNum[i] != sNum[j]:
            return False
        i = i + 1
        j = j - 1

    return True
"""
largestPal = 0

    for i in range(100, 1000):
    for j in range (100, 1000):
    if (isPalindrome(i * j) and i * j > largestPal):
    largestPal = i * j
""" #906609

# 5: What is the smallest positive number that is evenly divisible by all of
#    the numbers from 1 to 20?

# must be divisible by all the primes in that range
# -> must be divisible by (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19) = 9699690

# 1. begin with 9699690
# 2. test for divisibility of 1-20
# 3. if an integer btw 1-20 is not found to be evenly divisible, add 9699690
# -----repeat steps 2 & 3 until a number is found that satisfies the condition

def isEvenlyDivisibleByAll(num, rangemax):

    for i in range(2, rangemax + 1):
        if (num % i != 0):
            return False

    return True

def getSmallestPossibleNumberEvenlyDivisible(num):

    #collect list of prime divisors
    primeDivisors = []
    
    for i in range (2, num + 1):
        if isPrime(i):
            primeDivisors.append(i)

    primeDivisorProduct = 1
    #multiply iteratively by each prime divisor to get smallest number
    #divisible by all primes in range
    for x in primeDivisors:
        primeDivisorProduct = primeDivisorProduct * x

    smallNum = primeDivisorProduct

    haveSmallest = False

    while haveSmallest == False:
        if isEvenlyDivisibleByAll(smallNum, num):
            haveSmallest = True
        else:
            smallNum = smallNum + primeDivisorProduct

    return(smallNum)
                
#getSmallestPossibleNumberEvenlyDivisible(20) #232792560













































