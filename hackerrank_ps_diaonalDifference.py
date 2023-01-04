def diagonalDifference(arr):
    # Write your code here
    lr_sum =0
    rl_sum =0
    
    for i in range(len(arr)):
        #index from left to right of metrix = a[i][i]
        lr_sum = lr_sum + arr[i][i]
        #index from right to left of metrix = a[i][len(arr)-i-1] in that len(arr)-i-1 will make sure that the column index is returning backward with positive value
        rl_sum = rl_sum + arr[i][len(arr)-i-1]
    return abs(lr_sum - rl_sum)