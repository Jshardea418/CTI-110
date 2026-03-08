# Morgan Johnson
# 02/28/2026
# P1HW1
# This program collects numbers from the user,
# performs calculations, and displays the results.

print("-----Calculating Exponents-----")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print(base, "raised to the power of", exponent, "is", result, "!!")

print("\n-----Addition and Subtraction-----")

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

sum_total = num1 + num2
final_total = sum_total - num3

print(num1, "+", num2, "-", num3, "is equal to", final_total)
