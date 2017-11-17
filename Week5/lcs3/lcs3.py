#Uses python3




##-----------------------------------------------------------------##


              #############################################
              #######  Longest Subsequence Problem  #######
              #######       Recursive Solution      #######
              #######   Time Complexity => O(3^n)   #######
              #############################################



## This is a recursive implementation for the "Longest Subsequence
## Problem".
## Time Complexity => O(3^n)


## Step 1 -> Base case: If any of the indices becomes zero, i.e, 
##           length of the substring becomes 0, then return 0.
## Step 2 -> Recursive case: Check for the equality of element at
##           the index, if TRUE add 1, else add 0.



def longest_subsequence_recursive(a,b,i,j):


	# Base case
	# returns 0 if any of the index becomes 0
	# If length of any of the sub string is less than or
	# equals 0, return 0.
	if ((i < 0) or (j < 0)):
		return 0
	# If none of the substrings are NULL, then compare the elements
	# at the indices, and add 1 to the answer if they are equal else
	# return the value unchanged.
	else:
		if a[i] == b[j]:
			return (1 + max(longest_subsequence_recursive(a,b,i,j-1),
				            longest_subsequence_recursive(a,b,i-1,j),
				            longest_subsequence_recursive(a,b,i-1,j-1)
				            )
			        )
		else:
			return (max(longest_subsequence_recursive(a,b,i,j-1),
				        longest_subsequence_recursive(a,b,i-1,j),
				        longest_subsequence_recursive(a,b,i-1,j-1)
				        )
			        )







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
    n,*a = list(map(int, input()))
    m,*b = list(map(int, input()))
    l,*c = list(map(int, input()))
    
    print(a,b,c,end = '\n')
    print(longest_subsequence_recursive(a, b, n-1,m-1))



##-----------------------------------------------------------------##