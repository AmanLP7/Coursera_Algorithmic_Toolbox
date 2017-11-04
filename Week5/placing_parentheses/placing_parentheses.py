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
def MinAndMax(i,j):
    minVal = -float("Inf")
    maxVal = float("Inf")

    #Loop to calculate minimum and maximum value
    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], operator[k])
        b = evalt(M[i][k], m[k+1][j], operator[k])
        c = evalt(m[i][k], M[k+1][j], operator[k])
        d = evalt(m[i][k], m[k+1][j], operator[k])

        minMax = [min(minVal, a, b, c, d), max(maxVal, a, b, c, d)]


    return(minMax)





## Function to get maximum value using dynamic programming.
def get_maximum_value(dataset):




##-------------------------------------------------------------------##


if __name__ == "__main__":
    expression = list(input())
    digit = expression[0:len(expression)+1:2]
    operator = expression[1:len(expression)+1:2]
    print(digit,operator)



##-------------------------------------------------------------------##