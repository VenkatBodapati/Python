# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

rand_value = random.randint(0,len(names)-1)

#print(rand_value)
#print(len(names))

payer = names[rand_value]

print(f"{payer} is going to buy the meal today!")


