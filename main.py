#######################COFFEE MACHINE#######################
from menu import MENU, resources
from art import logo

def calc(flavour, money_inserted):
    cost_to_pay = MENU[flavour]["cost"]
    if money_inserted >= cost_to_pay:
        change = money_inserted - cost_to_pay
        print(f"Here is ${round(change,2)} in change.")
        print(f"Here is your {flavour} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def coins(flavour):
    print("Please insert coins.")
    quaters = float(input("How many quaters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    money_inserted = quaters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    calc(flavour, money_inserted)


money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
command = True
while command:
    print(logo)
    flavour = input("What would you like? {espresso / latte / cappuccino}: ")
    if flavour == "latte" or flavour == "cappuccino":
        if water >= MENU[flavour]["ingredients"]["water"] and milk >= MENU[flavour]["ingredients"]["milk"] and coffee >= MENU[flavour]["ingredients"]["coffee"]:
            water = water - MENU[flavour]["ingredients"]["water"]
            milk = milk - MENU[flavour]["ingredients"]["milk"]
            coffee = coffee - MENU[flavour]["ingredients"]["coffee"]
            money = money + MENU[flavour]["cost"]
            coins(flavour)
        else:
            if water < MENU[flavour]["ingredients"]["water"]:
                print(f"Sorry! there is not enough Water.")
            elif milk < MENU[flavour]["ingredients"]["milk"]:
                print(f"Sorry! there is not enough Milk.")
            elif coffee < MENU[flavour]["ingredients"]["coffee"]:
                print(f"Sorry! there is not enough Coffee.")
    elif flavour == "espresso":
        if water >= MENU[flavour]["ingredients"]["water"] and coffee >= MENU[flavour]["ingredients"]["coffee"]:
            water = water - MENU[flavour]["ingredients"]["water"]
            coffee = coffee - MENU[flavour]["ingredients"]["coffee"]
            money = money + MENU[flavour]["cost"]
            coins(flavour)
        else:
            if water < MENU[flavour]["ingredients"]["water"]:
                print(f"Sorry! there is not enough Water.")
            elif coffee < MENU[flavour]["ingredients"]["coffee"]:
                print(f"Sorry! there is not enough Coffee.")
    elif flavour == 'report':
        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: ${money}")
    elif flavour == 'off':
        command = False
        exit()
