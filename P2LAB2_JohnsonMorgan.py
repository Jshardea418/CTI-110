# Morgan Johnson
# 03/08/2026
# P2LAB2
#This program uses a dictionary to store vehicle MPG values and calculates gas needed for a trip.
cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}
keys = cars.keys()
print(keys)
vehicle = input("Enter a vehicle from the list above: ")
print(f"The MPG for {vehicle} is {cars[vehicle]}")
miles = float(input("Enter the number of miles you will drive: "))
gallons = miles / cars[vehicle]
print(f"You will need {gallons: .2f} gallons of gas. ")
