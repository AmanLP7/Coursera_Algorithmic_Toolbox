#Uses python3


##-----------------------------------------------------------------##


               ############################################
               #######  Longest Subsequence Problem  ######
               #######   Time Complexity =>          ######
               ############################################


## This is the algorithm for computing the length of common sub-
## -sequence for three sequences.

## Input ->  Integers n,m,l, and sequences of length n,m,l
##           respectively.
## Output -> Non-negative integer p denoting length of common
##           subsequence.


## Below is the algorithm to compute the length of common
## subsequence for three given sequences, it employs dynamic
## programming.



def lcs3(a, b, c):
    
    return 



##-----------------------------------------------------------------##



if __name__ == '__main__':
    n,*a = list(map(int, input().split()))
    m,*b = list(map(int, input().split()))
    l,*c = list(map(int, input().split()))
    
    print(a,b,c,end = '\n')
    print(lcs3(a, b, c))
