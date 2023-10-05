#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def specialTriple():

    result = []

    for a in range(1, 999):
        for b in range(1, 999 - a):
            c = 1000 - a - b
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    result.append(a)
                    result.append(b)
                    result.append(c)
                    return(result)

sideLengths = specialTriple()
                    
product = 1

for x in sideLengths:
    product = product * x

print(product)
