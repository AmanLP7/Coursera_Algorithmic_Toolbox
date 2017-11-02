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



## Function to evaluate expression                 
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False



## Function to get maximum value using dynamic programming.
def get_maximum_value(dataset):
    #write your code here
    return 0



##-------------------------------------------------------------------##


if __name__ == "__main__":
    print(get_maximum_value(input()))
