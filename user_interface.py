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
    while choice != "espresso" and choice != "latte" and choice != "cappuccino" and choice != "off" and choice != "report":
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

def give_response(drink, response):
    if response == main.RESPONSE_CODES["OK"]:
        print(f"Thank you! Here is your {drink}!")
    elif response == main.RESPONSE_CODES["FUNDS ERROR"]:
        print(f"Sorry. That's not enough money to purchase a {drink}. Here is your money back.")
    elif response == main.RESPONSE_CODES["INSUFFICIENT WATER ERROR"]:
        print(f"Sorry, not enough water to make {drink}. Here is your money back. Please add more water.")
    elif response == main.RESPONSE_CODES["INSUFFICIENT COFFEE ERROR"]:
        print(f"Sorry, not enough coffee to make {drink}. Here is your money back. Please add more coffee.")
    elif response == main.RESPONSE_CODES["INSUFFICIENT MILK ERROR"]:
        print(f"Sorry, not enough milk to make {drink}. Here is your money back. Please add more milk.")
    else:
        print(f"Thank you! Here is your {drink}!")
        print(f"Your change is ${response}")

def execute_choice(choice):
    if choice == "off":
        return False
    elif choice == "report":
        print_report()
        return True
    elif choice in main.MENU:
        money = prompt_for_money()
        if len(money) != 0:
            response_code = main.request_drink(money["Pennies"], money["Nickels"], money["Dimes"], money["Quarters"], choice)
            give_response(choice, response_code)
        return True


###########################################################################################

user_command = ""

on = prompt_to_turn_on(user_command)

while on:
    user_command = prompt_for_drink()
    on = execute_choice(user_command)