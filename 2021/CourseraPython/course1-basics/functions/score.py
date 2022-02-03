# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

answer = input("Enter Score: ")
score = float(answer)

# score has to be  between 0.0 and 1.0 
if score >=0.0 and score <=1.0:
    if score >= 0.9:
        grade = 'A' 
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    elif score < 0.6:
        grade = 'F'
    print(grade)
else:
    print("ERROR")

