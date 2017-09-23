# Uses python3

from random import randint

# lowest common multiple naive solution
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


# Euclidean algorithm
def gcd_Euclidean(a,b):
    while(b > 0):
        return gcd_Euclidean(b,a%b)
    return a


# Lcm using GCD
def lcm_using_gcd(a,b):
    gcd = gcd_Euclidean(a,b)

    lcm = (a * b) / gcd

    return(int(lcm))


a,b = sorted(map(int,input().split(" ")))[::-1]

print(lcm_using_gcd(a,b))
