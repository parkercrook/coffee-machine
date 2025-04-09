import main
import art

ERROR_CODES = {
}

def prompt_to_turn_on(command):
    while command != "on":
        command = input("Hello. Please type 'on' to turn on... ").lower()
    print("\n" * 20)
    print(art.logo)
    return True

def prompt_for_drink():
    choice = ""
    while choice != "espresso" and choice != "latte" and choice != "capuccino" and choice != "off" and choice != "report":
        choice = input("What can I make for you? (espresso/latte/cappuccino): ").lower()
    return choice

def print_report():
    for resource in main.resources:
        print(f"{resource.upper()}: {main.resources[resource]}")

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


def execute_choice(choice):
    if choice == "off":
        return False
    elif choice == "report":
        print_report()
        return True
    elif choice == "espresso":
        money = prompt_for_money()
        if len(money) == 0:
            return True
        else:
            print(main.request_espresso(money["Pennies"], money["Nickels"],money["Dimes"], money["Quarters"]))
            return True


###########################################################################################

user_command = ""

on = prompt_to_turn_on(user_command)

while on:
    user_command = prompt_for_drink()
    on = execute_choice(user_command)