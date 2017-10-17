# Uses python3
import random


##=========================================================##

         ########################################
         ##### Knapscak without repititions #####
         #####    Time complexity => O(n)   #####
         ########################################


## Step 1 -> Take a two dimensional array, having length W, 
##           and breadth n.

## Step 2 -> 



def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


##=========================================================##


if __name__ == '__main__':
    W, n, *w = list(map(int, input().split(" ")))
    print(W,n,w)


##=========================================================##