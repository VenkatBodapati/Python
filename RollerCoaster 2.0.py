print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height > 120:
    age = int(input("Please enter your age: "))
    if age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    else:
        bill = 12
    photos = str(input("Do you need photos during your ride? type yes or no "))
    if photos == 'yes':
        bill += 3
    else:
        bill = bill
    print(f"Your final bill is ${bill}")
else:
    print("Sorry! you have to grow little taller to have a ride")