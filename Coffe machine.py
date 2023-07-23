MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 100,
}


water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

quarters = 0
dimes = 0
nickles = 0
pennies = 0

resource_short = ''

while water > 0 and milk > 0 and coffee > 0:

    customer_choice = input("What would you like? (espresso/latte/cappuccino)").lower()

    if customer_choice == 'report':
        print(f"water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    if customer_choice == 'off':
        break

    if customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":
        water2 = MENU[customer_choice]["ingredients"]["water"]
        if customer_choice == "espresso":
            milk2 = 0
        else:
            milk2 = MENU["cappuccino"]["ingredients"]["milk"]
        coffee2 = MENU[customer_choice]["ingredients"]["coffee"]
        cost = MENU[customer_choice]["cost"]
        if water > water2 and milk > milk2 and coffee > coffee2:
            print("Please insert coins.")
            quarters_inserted = int(input("How many quarters?: "))
            dimes_inserted = int(input("How many dimes?: "))
            nickles_inserted = int(input("How many nickles?: "))
            pennies_inserted = int(input("How many pennies?: "))
            Total_money_inserted = ((quarters_inserted * 0.25) + (dimes_inserted * 0.10) +
                                    (nickles_inserted * 0.05) + (pennies_inserted * 0.01))
            if Total_money_inserted > cost:
                change = round((Total_money_inserted - cost), 2)
                water -= water2
                milk -= milk2
                coffee -= coffee2
                money += cost
                print(f"Here is ${change} in change.")
                print(f"Here is your {customer_choice} ! Enjoy")
            else:
                print("Sorry! That's not enough money. Money refunded")
        else:
            if water < water2:
                resource_short = 'water'
            elif milk < milk2:
                resource_short = 'milk'
            else:
                resource_short = 'coffee'

            print(f"Sorry, there is not enough {resource_short}")
            break
"""
    if customer_choice == "espresso":
        water2 = MENU["espresso"]["ingredients"]["water"]
        milk2 = 0
        coffee2 = MENU["espresso"]["ingredients"]["coffee"]
        cost = MENU["espresso"]["cost"]
        if water > water2 and milk > milk2 and coffee > coffee2:
            print("Please insert coins.")
            quarters_inserted = int(input("How many quarters?: "))
            dimes_inserted = int(input("How many dimes?: "))
            nickles_inserted = int(input("How many nickles?: "))
            pennies_inserted = int(input("How many pennies?: "))
            Total_money_inserted = ((quarters_inserted * 0.25) + (dimes_inserted * 0.10) +
                                    (nickles_inserted * 0.05) + (pennies_inserted * 0.01))
            if Total_money_inserted > cost:
                change = round((Total_money_inserted - cost), 2)
                water -= water2
                milk -= milk2
                coffee -= coffee2
                money += cost
                print(f"Here is ${change} in change.")
                print(f"Here is your {customer_choice} ! Enjoy")
            else:
                print("Sorry! That's not enough money. Money refunded")
        else:
            if water < water2:
                resource_short = 'water'
            elif milk < milk2:
                resource_short = 'milk'
            else:
                resource_short = 'coffee'

            print(f"Sorry, there is not enough {resource_short}")
            break

    if customer_choice == "latte":
        water2 = MENU["latte"]["ingredients"]["water"]
        milk2 = MENU["latte"]["ingredients"]["milk"]
        coffee2 = MENU["latte"]["ingredients"]["coffee"]
        cost = MENU["latte"]["cost"]
        if water > water2 and milk > milk2 and coffee > coffee2:
            print("Please insert coins.")
            quarters_inserted = int(input("How many quarters?: "))
            dimes_inserted = int(input("How many dimes?: "))
            nickles_inserted = int(input("How many nickles?: "))
            pennies_inserted = int(input("How many pennies?: "))
            Total_money_inserted = ((quarters_inserted * 0.25) + (dimes_inserted * 0.10) +
                                    (nickles_inserted * 0.05) + (pennies_inserted * 0.01))
            if Total_money_inserted > cost:
                change = round((Total_money_inserted - cost), 2)
                water -= water2
                milk -= milk2
                coffee -= coffee2
                money += cost
                print(f"Here is ${change} in change.")
                print(f"Here is your {customer_choice} ! Enjoy")
            else:
                print("Sorry! That's not enough money. Money refunded")
        else:
            if water < water2:
                resource_short = 'water'
            elif milk < milk2:
                resource_short = 'milk'
            else:
                resource_short = 'coffee'

            print(f"Sorry, there is not enough {resource_short}")
            break

    if customer_choice == "cappuccino":
        water2 = MENU["cappuccino"]["ingredients"]["water"]
        milk2 = MENU["cappuccino"]["ingredients"]["milk"]
        coffee2 = MENU["cappuccino"]["ingredients"]["coffee"]
        cost = MENU["espresso"]["cost"]
        if water > water2 and milk > milk2 and coffee > coffee2:
            print("Please insert coins.")
            quarters_inserted = int(input("How many quarters?: "))
            dimes_inserted = int(input("How many dimes?: "))
            nickles_inserted = int(input("How many nickles?: "))
            pennies_inserted = int(input("How many pennies?: "))
            Total_money_inserted = ((quarters_inserted * 0.25) + (dimes_inserted * 0.10) +
                                    (nickles_inserted * 0.05) + (pennies_inserted * 0.01))
            if Total_money_inserted > cost:
                change = round((Total_money_inserted - cost), 2)
                water -= water2
                milk -= milk2
                coffee -= coffee2
                money += cost
                print(f"Here is ${change} in change.")
                print(f"Here is your {customer_choice} ! Enjoy")
            else:
                print("Sorry! That's not enough money. Money refunded")
        else:
            if water < water2:
                resource_short = 'water'
            elif milk < milk2:
                resource_short = 'milk'
            else:
                resource_short = 'coffee'

            print(f"Sorry, there is not enough {resource_short}")
            break
"""





