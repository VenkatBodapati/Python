# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()

HighScore = 0
Score = 0

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    Score = student_scores[n]
    if HighScore < Score:
        HighScore = Score    
    
    
print(student_scores)

print(HighScore)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇




