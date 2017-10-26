                   

                 ###############################
                 ###  Edit distance problem  ###
                 ###############################


import random


##-------------------------------------------------------------------##


              ######################################
              ## Edit distance recursive solution ##
              ####  Time Complexity => O(3^n)   ####
              ######################################




## This is the recursive solution to edit distance problem.

## Problem Definition =>
## Edit distance between two strings is the minimum number of 
## insertion, deletions and mismatches in the alignment of two
## strings.

def edit_distance_recursive(string1, string2, m, n):

	# If the first string is empty then we'll have to insert
	# all the characters of second string in the first one.
	if (m == 0):
		return n

	# If the second string is empty then we'll have to delete
	# all the characters in the first string.
	elif (n == 0):
		return m

	# If the last characters of the two strings are identical,
	# then we ignore them and compare the remaining substring.
	elif (string1[m-1] == string2[n - 1]):
		return(edit_distance_recursive(string1, string2, m-1, n-1))

	# Else we find out which process among insertion, deletion,
	# or mismatch incurs minimum cost.
	else:
		return(1 + 
			   min(edit_distance_recursive(string1,string2,m,n-1),
			   	   edit_distance_recursive(string1,string2,m-1,n-1),
			   	   edit_distance_recursive(string1,string2,m-1,n)
			   	   )
			   )




##-------------------------------------------------------------------##



if __name__ == "__main__":
	string1 = input().split(" ")
	string2 = input().split(" ")

	print(edit_distance_recursive(string1, string2, 
		                          len(string1), len(string2)))




##-------------------------------------------------------------------##
