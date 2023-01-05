a = [5,5,5,5,5]

def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    total = sum(arr)
    for i in range(len(arr)):
        if arr[i] == max(arr):
            min_sum = total - arr[i]
        if arr[i] == min(arr):
            max_sum = total - arr[i]
    return print(min_sum, max_sum)
    
miniMaxSum(a)

# print(max([5,5,5,5,5]))
# print(min([5,5,5,5,5]))