def plusMinus(arr):
    # Write your code here
    p_positive = 0
    p_negative = 0
    p_zero = 0
    
    
    for i in range(len(arr)):
        if arr[i] == 0: 
            p_zero += 1
        elif arr[i] > 0:
            p_positive += 1
        else: 
            p_negative += 1
            
    n1 =round(p_positive/len(arr),6)
    n2 =round(p_negative/len(arr),6)
    n3 =round(p_zero/len(arr),6)            
    print(n1)
    print(n2)
    print(n3)     
