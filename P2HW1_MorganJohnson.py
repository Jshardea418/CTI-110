# Morgan Johnson
# March 15, 2026
#P2HW1 - Travel Budget
# This program calculates and displays travel expenses in a formatted output.
print("This program calculates and displays travel expenses")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))
expenses = gas + accommodation + food
remaining = budget - expenses
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${accommodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining:,.2f}")