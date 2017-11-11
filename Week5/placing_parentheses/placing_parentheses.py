# Uses python3


##-------------------------------------------------------------------##


                 #####################################
                 ######   Placing parantheses   ######
                 ######  Time Complexity =>     ######
                 #####################################


## Input -> String S, of length 2n+1 for some n, with symbols s(0),
##          s(1),s(2),.....,s(2n). Symbol at even position of S is a
##          digit, symbol at odd position is one of three operations
##          {+,-,*}.
## Output -> Maximum possible value of arithmetic expression.


## Function used ==>> 
## 
## 1. evalt() - It performs the given operation on an expression.
## 
## 2. MinAndMax() - It calculates the maximum and minimum value for
##                  a sub-expression.
##
## 3. get_maximum_value() - It calculates the maximum possible value
##                          for an expression by reordering, 
##                          parantheses.  

## Steps involved ==>>
## 
## Step 1 -> Initialise two square matrices of length n, "m" and "M".
## Step 2 -> Fill diagnol elements of both the matrices with the their
##           respective digit in the "digits" array. 




## Function to perform given operation on an expression                
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False






## Function to calculate minimum and maximum value for an expression.
## The function returns a list whose first value is the minimum value,
## and the second value is a maximum value.
def MinAndMax(i,j,digits,operators):

    minVal = float("Inf")
    maxVal = -float("Inf")

    #Loop to calculate the minimum and maximum value for
    #a given subexpression
    for k in range(i,j-1):
        a = evalt(M[i][k],M[k+1][j],operators[k])
        b = evalt(M[i][k],m[k+1][j],operators[k])
        c = evalt(m[i][k],M[k+1][j],operators[k])
        d = evalt(m[i][k],m[k+1][j],operators[k])






## Function to get maximum value using dynamic programming.
def get_maximum_value(digits, operators):

    n = len(digits)

    #Initialising min and max matrices
    m = [[0 for i in range(n)] for j in range(n)]
    M = [[0 for i in range(n)] for j in range(n)]

    #Filling diagnol elements with corresponding elements in
    #"digits" list.
    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]


    for rows in m:
        print(*rows,end=' ')
        print('\n')
    for rows in M:
        print(*rows,end=' ')
        print('\n')


    #Loop to calculate the maximum value of an expression
    for s in range(n-1):
        for i in range(n-s):
            j = i+s
            m[i][j],M[i][j] = MinAndMax(i,j)


    return (M[1][n-1])
    




##-------------------------------------------------------------------##





if __name__ == "__main__":
    expression = list(input())
    digits = [int(x) for x in expression[0:len(expression)+1:2]]
    operators = expression[1:len(expression)+1:2]
    print(digits,operators)
    get_maximum_value(digits,operators)




##-------------------------------------------------------------------##