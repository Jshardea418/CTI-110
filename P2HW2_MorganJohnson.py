# Morgan Johnson
# March 15, 2026
# P2HW2 - Lists
# This program asks the user to enter grades for six modules,
# stores them in a list, and displays the lowest grade, highest grade, 
# sum of grades, and the average.
# Pseudocode
# 1. Create an empty list to store grades
# 2. Ask the user to enter grades for Module 1 through Module 6
# 3. Convert each grade to float and add it to the list
# 4. Find the lowest grade using min()
# 5. Find the highest grade using max()
# 6. Find the sum of all grades using sum()
# 7. Calculate the average by dividing the sum by the number of grades
# 8. Display the results formatted neatly with the average shown to two decimal places
# Create empty list
module_grades = []

# Ask user for grades
module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

# Calculations
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Output
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade}")
print(f"{'Highest Grade:':<20}{highest_grade}")
print(f"{'Sum of Grades:':<20}{total}")
print(f"{'Average:':<20}{average:.2f}")
print("-------------------------------")
