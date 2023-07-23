# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

name_lower_case = name1_lower_case + name2_lower_case

TrueCnt = str(name_lower_case.count("t") + name_lower_case.count("r") + name_lower_case.count("u") + name_lower_case.count("e"))

LoveCnt = str(name_lower_case.count("l") + name_lower_case.count("o") + name_lower_case.count("v") + name_lower_case.count("e"))

TrueLoveCnt = int(TrueCnt + LoveCnt)

#print(TrueLoveCnt)

if TrueLoveCnt  < 10 or TrueLoveCnt > 90:
    print(f"Your score is {TrueLoveCnt}, you go together like coke and mentos.")
elif TrueLoveCnt  >= 40 and TrueLoveCnt <= 50:
    print(f"Your score is {TrueLoveCnt}, you are alright together.")
else:
    print(f"Your score is {TrueLoveCnt}")


