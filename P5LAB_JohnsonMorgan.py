# Morgan Johnson
# 4/26/2026
# P5LAB
# Self-checkout change calculator

import random


def disperse_change(change):

    change = round(change * 100)

    dollars = change // 100
    change = change % 100

    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change

    print("\nChange breakdown:")
    print("Dollars:", dollars)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)


def main():

    owed = round(random.uniform(0.01, 100.00), 2)
    print("You owe: $", owed)

    payment = float(input("Enter cash amount: $"))

    change = payment - owed

    if change < 0:
        print("Not enough money provided.")
    else:
        print("Change owed: $", round(change, 2))
        disperse_change(change)


main()
