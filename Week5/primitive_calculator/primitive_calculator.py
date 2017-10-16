# Uses python3
import random


##============================================================##

                #######################################
                ########   Greedy Solution    #########
                ######  Time Complexity => O(n)  ######
                #######################################



## This is a greedy solution to the primitive algorithm
## problem. It is incorrect


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


##============================================================##


          ################################################
          ########  Dynamic Programming Solution  ########
          ##########  Time Complexity => O(n)  ###########
          ################################################


## Step 1 -> Take an array "steps" of length n+1 and initialise
##           the first two elements with zeros, and all the other
##           elements with float("Inf").

## Step 2 -> Take another array "sequence" and initialise, it 
##           will be used to store the sequence in which operation
##           proceed.


def optimal_sequence(n):
	steps = [0]*2
	steps.extend([float("Inf")] * (n-1))

	sequence = []


	# Filling the steps array

	for i in range(2,n+1):
		if (i % 6 == 0):
			steps[i] = min(steps[i // 3], steps[i // 2],
				           steps[i - 1]) + 1
		elif (i % 3 == 0):
			steps[i] = min(steps[i // 3], steps[i - 1]) + 1
		elif (i % 2 == 0):
			steps[i] = min(steps[i // 2], steps[i - 1]) + 1
		else:
			steps[i] = steps[i-1] + 1


    return(steps[n])


##============================================================##


n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')



##============================================================##