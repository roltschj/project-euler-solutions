# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def getSumOfSquares(num):

    result = 0

    for i in range(num + 1):
        result = result + i**2

    return result

def getSquareOfSum(num):

    sum = 0

    for i in range(num + 1):
        sum = sum + i

    return sum**2

print(getSquareOfSum(100) - getSumOfSquares(100)) #25164150
