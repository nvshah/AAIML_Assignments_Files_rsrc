def gcd(a, b):
    '''Eucledian Algo to find HCF'''
    a, b = min(a,b), max(a,b)
    if not a: 
        return b 

    return gcd(a, b % a)

# def computeHCF(a, b):
#     small = min(a, b)

#     hcf = 1


print(gcd(270, 192))


