# Uses python3


from random import randint

# naive algorithm for calculating gcd
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# Euclidean algorithm
def gcd_Euclidean(a,b):
    while(b > 0):
        return gcd_Euclidean(b,a%b)
    return a

a,b = sorted(map(int,input().split(" ")))[::-1]

if b == 0:
    print(1)
else:
    print(gcd_Euclidean(a,b))
