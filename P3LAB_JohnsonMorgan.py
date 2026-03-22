# Morgan Johnson
# March 22, 2026
# P3LAB_JohnsonMorgan.py
# This program calculates the most effecient number
# of dollars and coins for a given money amount.
amount = float(input("Enter a money value (e.g., 1.23): "))
total_cents = int(amount * 100)
dollars = total_cents // 100
total_cents -= dollars * 100
quarters = total_cents // 25
total_cents -= quarters * 25
dimes = total_cents // 10
total_cents -= dimes * 10
nickels = total_cents // 5
total_cents -= nickels * 5
pennies = total_cents
if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(dollars, "dollars")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(quarters, "quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(dimes, "dimes")

if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(nickels, "nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(pennies, "pennies")