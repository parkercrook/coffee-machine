import main
import art

def prompt_to_turn_on(command):
    while command != "on":
        command = input("Hello. Please type 'on' to turn on... ").lower()
    print("\n" * 20)
    print(art.logo)
    return True

def prompt_for_drink():
    choice = ""
    while choice != "espresso" and choice != "latte" and choice != "cappuccino" and choice != "off" and choice != "report" and choice != "refill":
        choice = input("What can I make for you? (espresso/latte/cappuccino): ").lower()
    return choice

def print_report():
    for resource in main.resources:
        print(f"{resource.upper()}: {main.resources[resource]}")
    print(f"Money available: ${main.total_money}")

def prompt_for_money():
    money_given = {}
    try:
        money_given = {
            "Pennies": int(input("How many pennies?: ")),
            "Nickels": int(input("How many nickels?: ")),
            "Dimes": int(input("How many dimes?: ")),
            "Quarters": int(input("How many quarters?: "))
        }
    except ValueError:
        print("Error. Not a valid amount of coins.")
    return money_given

def give_response(drink, response, change=0.0, missing_resources=None):
    if missing_resources is None:
        missing_resources = []
    if response == main.RESPONSE_CODES["FUNDS ERROR"]:
        print(f"Sorry. That's not enough money to purchase a {drink}. Here is your money back.")
    elif response == main.RESPONSE_CODES["INSUFFICIENT RESOURCE ERROR"]:
        print("Sorry, there's not enough: ")
        for resource in missing_resources:
            print(f"--> {resource}")
        print("Please refill the needed ingredients.")
    elif response == main.RESPONSE_CODES["GIVE CHANGE"]:
        print(f"Thank you! Here is your ☕ {drink}!")
        if change > 0.0:
            print(f"Your change is ${change}")
    elif response == main.RESPONSE_CODES["OK"]:
        print("Request was successful!")

def execute_choice(choice):
    if choice == "off":
        return False
    elif choice == "report":
        print_report()
        return True
    elif choice == "refill":
        response = main.refill_resources()
        give_response(choice, response)
        return True
    elif choice in main.MENU:
        resource_response_code = main.check_enough_resources(choice)
        if resource_response_code  == main.RESPONSE_CODES["OK"]:
            money_given = prompt_for_money()
            funds_response_code = main.check_enough_funds(money_given, choice)
            if funds_response_code == main.RESPONSE_CODES["GIVE CHANGE"]:
                change = main.give_change(money_given, choice)
                main.make_drink(choice)
                give_response(choice, funds_response_code, change)
            else:
                give_response(choice, funds_response_code)
        else:
            missing_resources = main.get_missing_resources(choice)
            give_response(choice, resource_response_code, missing_resources=missing_resources)

        return True

################################################## PROGRAM START ##################################################

user_command = ""
on = prompt_to_turn_on(user_command)
while on:
    user_command = prompt_for_drink()
    on = execute_choice(user_command)