resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

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
}

PENNY_VALUE = 0.01
NICKEL_VALUE = 0.05
DIME_VALUE = 0.10
QUARTER_VALUE = 0.25

def convert_coins(pennies, nickels, dimes, quarters):
    return (pennies * PENNY_VALUE) + (nickels * NICKEL_VALUE) + (dimes * DIME_VALUE) + (quarters * QUARTER_VALUE)

def give_change(total_received, drink_cost):
    return total_received - drink_cost

def check_enough_funds(p, n, d, q, drink_requested):
    money = convert_coins(p, n, d, q)
    if money < MENU[drink_requested]["cost"]:
        return RESPONSE_CODES["FUNDS ERROR"]
    elif money == MENU[drink_requested]["cost"]:
        return RESPONSE_CODES["OK"]
    elif money  > MENU[drink_requested]["cost"]:
        return give_change(money, MENU[drink_requested]["cost"])


def request_espresso(p, n, d, q):
    response = check_enough_funds(p, n, d, q, "espresso")
    if response == RESPONSE_CODES["OK"]:
        return "success"
    else:
        return "fail"



