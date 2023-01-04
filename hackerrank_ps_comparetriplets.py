def compareTriplets(a, b):
    # Write your code here
    bob_a = 0
    alice_b = 0 
   
    while len(a) <= 3 and len(b) <=3:
        for i in range(len(a)):
                if a[i] > b[i]: 
                    alice_b += 1
                elif a[i] < b[i]: 
                    bob_a += 1
                
        
        return [alice_b,bob_a]  