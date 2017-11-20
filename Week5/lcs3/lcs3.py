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
##           the index i,j, cases are as follows:
##           If equal: add 1 to the return value,
##           and check if it is less than or equal to min(i,j),
##           if TRUE return 1 + ans, else return ans
##           If not equal : return ans.
##           Note that the the maximum possible length of the
##           substring cannot be greater than the length of smaller
##           of two strings being compared



def lcs_recursive(a,b,i,j):


	# Base case:
	# returns 0 if any of the index becomes 0
	# If length of any of the sub string is less than or
	# equals 0, return 0.
	if (i < 0 or j < 0):
		return 0


	# Recursive case:
	# If none of the substrings are NULL, then add 1 to the
	# returned value of subproblem, and check whether it is
	# equal to or less than the length of smallest substring,
	# if TRUE keep the ans and return it, else, return the 
	# original ans of the subproblem.
	else:
		ans = max(lcs_recursive(a,b,i-1,j),
			      lcs_recursive(a,b,i,j-1),
			      lcs_recursive(a,b,i-1,j-1))

		if ((1+ans) <= min(i,j)):
			return (1+ans)
		else:
			return

	

	


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
    print(lcs_recursive(a, b, n-1,m-1))



##-----------------------------------------------------------------##