# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

sp = 15
mp = 20
lp = 25

bill = 0

if size == 'S':
    bill = sp
elif size == 'M':
    bill = mp
else:
    bill = lp

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill+= 3

if extra_cheese == 'Y':
    bill+= 1

print(f"Your final bill for selected Pizza is : ${bill}")






