MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
Money = 0

print("COFFEE MACHINE")
endcm = False
def report():
    """Reports the quantity of resources left."""
    global resources
    global Money
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${Money}")

def checkres(x):
    """Checks if resources are enough for user coffee choice."""
    global resources
    copt = MENU[x]
    i = copt["ingredients"]
    m = i["milk"]
    w = i["water"]
    c = i["coffee"]
    if m > resources["milk"] or w > resources["water"] or c > resources["coffee"]:
        print("Sorry. There is not enough:")
        if m > resources["milk"]:
            print("milk")
        if w > resources["water"]:
            print("water")
        if c > resources["coffee"]:
            print("coffee")
        return False
    return True

def checkcoins(x):
    """Collects and Processes coins inserted and checks for successful transaction."""
    global resources
    global Money
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))*0.25
    dimes = int(input("How many dimes?: "))*0.10
    nickles = int(input("How many nickles?: "))*0.05
    pennies = int(input("How many pennies?: "))*0.01
    y = quarters + dimes + nickles + pennies
    
    copt = MENU[x]
    c = copt["cost"]
    if y > c:
        Money += c
        change = round(y - c, 2)
        print(f"Here is your change: ${change}")
        return True
    elif y < c:
        print(f"Sorry. Coins are not enough!\nMoney refunded: ${y}.")
        return False

def cm():
    """Function that makes the coffee."""
    global endcm
    opt = input("What would you like? (espresso/latte/cappuccino)\n")

    if opt == "report":
        report()
    elif opt == "off":
        endcm = True
    elif opt == "espresso" or opt == "latte" or opt == "cappuccino":
        if checkres(opt):
            if checkcoins(opt):
                copt = MENU[opt]
                i = copt["ingredients"]
                m = i["milk"]
                w = i["water"]
                c = i["coffee"]
                resources["milk"] -= m
                resources["water"] -= w
                resources["coffee"] -= c
                print(f"Enjoy your {opt}.☕")
    else:
        print("You have typed a wrong input!")
        
while not endcm:
    cm()
    
