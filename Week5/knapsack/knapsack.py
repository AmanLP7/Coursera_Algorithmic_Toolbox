# Uses python3
import random


##=========================================================##

         #########################################
         ##### Knapsack without repititions ######
         #####    Time complexity => O(nW)   #####
         #########################################


## Step 1 -> Take a two dimensional array, having length W, 
##           and breadth n.

## Step 2 -> Fill the "value" matrix using following logic,
##           
##           Case 1 -> nth item is included in solution so,
##                     the subproblem is knapsack of weight
##                     W - w(n), using items 1,2,...,n-1
##           Case 2 -> nth item is not included then whole
##                     knapsack must be filled with items
##                     1,2,....n-1.



def optimal_weight(W, w):
    
    # knapsack matrix
    value = [[0 for x in range(W+1)]
                       for y in range(len(w) + 1)]



    for i in range(1, len(w) + 1):
    	for weights in range(1, W+1):
    		value[i][weights] = value[i-1][weights]
    		if w[i-1] <= weights:
    			val = value[i-1][weights-w[i-1]] + w[i-1]
    			if value[i][weights] < val:
    				value[i][weights] = val

    '''
    for rows in value:
    	print(*rows,end = " ")
    	print('\n')
    '''

    return(value[len(w)][W])
 
 

##=========================================================##

             ####################################
             ###  Knapsack without repitions  ###
             ###      recursive solution      ###
             ###   Time complexity => O()     ###
             ####################################



##=========================================================##

if __name__ == '__main__':
    W, n, *w = list(map(int, input().split(" ")))
    print(optimal_weight(W,w))


##=========================================================##