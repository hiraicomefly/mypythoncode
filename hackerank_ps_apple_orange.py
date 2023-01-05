def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    counta = 0
    counto = 0
     
    for i in range(len(apples)):
        if s <= apples[i] + a <= t:
            counta += 1
    for j in range(len(oranges)):
        if s <= oranges[j] + b <= t:
            counto += 1
                
    print(counta)
    print(counto)
