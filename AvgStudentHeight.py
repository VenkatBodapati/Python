# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# print(student_heights)
# print(len(student_heights))
total_height = 0
Avg_Height = 0

# for n in range(0, len(student_heights)):
#     height = int(student_heights[n])
for n in student_heights:
    height = int(n)
    # 🚨 Don't change the code above 👆   

    #  Write your code below this row 👇
    
    total_height = total_height + height

Avg_Height = round(total_height/len(student_heights))

print (f"Total Height is {total_height}")

print (f"Avg height is {Avg_Height}")



