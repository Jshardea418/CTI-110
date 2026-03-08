# Morgan Johnson
# 03/08/2026
# P2LAB1
# Program calculates the diameter, circumference, area of a circle given the radius
import math
radius = float(input("Enter the radius of the circle: "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
