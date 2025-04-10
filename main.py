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
    "INSUFFICIENT WATER ERROR": 2,
    "INSUFFICIENT COFFEE ERROR": 3,
    "INSUFFICIENT MILK ERROR":  4,
    "GIVE CHANGE": 5
}

PENNY_VALUE = 0.01
NICKEL_VALUE = 0.05
DIME_VALUE = 0.10
QUARTER_VALUE = 0.25

def convert_coins(pennies, nickels, dimes, quarters):
    return (pennies * PENNY_VALUE) + (nickels * NICKEL_VALUE) + (dimes * DIME_VALUE) + (quarters * QUARTER_VALUE)

def give_change(total_received, drink_cost):
    return round(total_received - drink_cost, 2)

def check_enough_funds(p, n, d, q, drink_requested):
    money = convert_coins(p, n, d, q)
    if money < MENU[drink_requested]["cost"]:
        return RESPONSE_CODES["FUNDS ERROR"]
    elif money == MENU[drink_requested]["cost"]:
        return RESPONSE_CODES["OK"]
    elif money  > MENU[drink_requested]["cost"]:
        return RESPONSE_CODES["GIVE CHANGE"]

def check_enough_resources(drink_choice):
    if "water" in MENU[drink_choice]["ingredients"]:
        if resources["water"] < MENU[drink_choice]["ingredients"]["water"]:
            return RESPONSE_CODES["INSUFFICIENT WATER ERROR"]

    if "coffee" in MENU[drink_choice]["ingredients"]:
        if resources["coffee"] < MENU[drink_choice]["ingredients"]["coffee"]:
            return RESPONSE_CODES["INSUFFICIENT COFFEE ERROR"]

    if "milk" in MENU[drink_choice]["ingredients"]:
        if resources["milk"] < MENU[drink_choice]["ingredients"]["milk"]:
            return RESPONSE_CODES["INSUFFICIENT MILK ERROR"]

    return RESPONSE_CODES["OK"]

def make_drink(drink):
    if "water" in MENU[drink]["ingredients"]:
        resources["water"] -= MENU[drink]["ingredients"]["water"]

    if "coffee" in MENU[drink]["ingredients"]:
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]



def request_drink(p, n, d, q, drink):
    resources_response = check_enough_resources(drink)
    money_given = convert_coins(p, n, d, q)
    funds_response = check_enough_funds(p, n, d, q, drink)

    if resources_response == RESPONSE_CODES["OK"]:
        if funds_response == RESPONSE_CODES["FUNDS ERROR"]:
            return funds_response
        else:
            make_drink(drink)
            global total_money
            total_money += MENU[drink]["cost"]
            if funds_response == RESPONSE_CODES["GIVE CHANGE"]:
                return give_change(money_given, MENU[drink]["cost"])
            else:
                return resources_response
    else:
        return resources_response



