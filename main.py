resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money = 20.0

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

RESPONSE_CODES = {
    "OK" : 0,
    "FUNDS ERROR" : 1,
    "INSUFFICIENT RESOURCE ERROR": 2,
    "GIVE CHANGE": 3
}

PENNY_VALUE = 0.01
NICKEL_VALUE = 0.05
DIME_VALUE = 0.10
QUARTER_VALUE = 0.25
MAX_WATER = 300
MAX_COFFEE_GROUNDS = 100
MAX_MILK = 200

def convert_coins(money_given):
    """Converts coins given into a total money value based on their individual values."""
    return (money_given["Pennies"] * PENNY_VALUE) + (money_given["Nickels"] * NICKEL_VALUE) + (money_given["Dimes"] * DIME_VALUE) + (money_given["Quarters"] * QUARTER_VALUE)

def give_change(money_given, drink):
    """Returns change by subtracting the chosen drink's cost by the money given."""
    drink_cost = MENU[drink]["cost"]
    total = convert_coins(money_given)
    return round(total - drink_cost, 2)

def add_funds_to_total(drink_cost):
    global total_money
    total_money += drink_cost

def check_enough_funds(money_given, drink_requested):
    """Checks that the user provided enough coins for the drink requested and returns a response code."""
    money = convert_coins(money_given)
    if money < MENU[drink_requested]["cost"]:
        return RESPONSE_CODES["FUNDS ERROR"]
    elif money >= MENU[drink_requested]["cost"]:
        add_funds_to_total(MENU[drink_requested]["cost"])
        return RESPONSE_CODES["GIVE CHANGE"]

def get_missing_resources(drink_choice):
    """Checks missing resources for the requested drink and returns a list of which are missing."""
    missing_resources = []
    if "water" in MENU[drink_choice]["ingredients"]:
        if resources["water"] < MENU[drink_choice]["ingredients"]["water"]:
            missing_resources.append("Water")

    if "coffee" in MENU[drink_choice]["ingredients"]:
        if resources["coffee"] < MENU[drink_choice]["ingredients"]["coffee"]:
            missing_resources.append("Coffee")

    if "milk" in MENU[drink_choice]["ingredients"]:
        if resources["milk"] < MENU[drink_choice]["ingredients"]["milk"]:
            missing_resources.append("Milk")

    return missing_resources


def check_enough_resources(drink_choice):
    """Checks that the machine contains enough resources for the drink requested and returns a response code."""
    missing_resources = get_missing_resources(drink_choice)
    if len(missing_resources) > 0:
        return RESPONSE_CODES["INSUFFICIENT RESOURCE ERROR"]
    else:
        return RESPONSE_CODES["OK"]

def make_drink(drink):
    """Removes needed ingredients from the machine's resources for the requested drink."""
    if "water" in MENU[drink]["ingredients"]:
        resources["water"] -= MENU[drink]["ingredients"]["water"]

    if "coffee" in MENU[drink]["ingredients"]:
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]

def refill_resources():
    resources["water"] = MAX_WATER
    resources["coffee"]  = MAX_COFFEE_GROUNDS
    resources["milk"] = MAX_MILK

    return RESPONSE_CODES["OK"]






