def gradingStudents(grades):
    # Write your code here
    final_grade = []
    for i in range(len(grades)):
        n = (grades[i] + (5-(grades[i] % 5)))
        if  grades[i] >= 38:
            if n - grades[i] < 3:
                final_grade.append(n)
            else: 
                n = grades[i]
                final_grade.append(n)
        if grades[i] < 38: 
            n = grades[i]
            final_grade.append(n)
    return final_grade             


m = [73,67,38,33]
print(gradingStudents(m))

#def round_to_next5(n):
#    return n + (5-n) % 5
#
#print(round_to_next5(2))

