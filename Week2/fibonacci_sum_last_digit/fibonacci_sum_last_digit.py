# Uses python3


from random import randint


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


# piasno period for n = 10 is 60
# Sum of first n Fibonacci numbers is given by :  F(0)+F(1)+F(2)+........+F(n) = F(n+2) - F(2)

def fibonacci_sum_fast(n):

    if n <= 1:
        return (n)

    index = (n+2) % 60
    previous = 0
    current = 1
    
    for _ in range(index-1):
        previous, current = current, previous + current
    
   
    last_digit = (current  - 1) % 10

    return(last_digit)



n = int(input())

print(fibonacci_sum_fast(n))

