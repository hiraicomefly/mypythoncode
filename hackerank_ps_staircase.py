def staircase(n):
    # Write your code here
    for i in range (1,n+1): 
        sp = n - i 
        print(" " * sp + "#" * i, sep="")

staircase(6)