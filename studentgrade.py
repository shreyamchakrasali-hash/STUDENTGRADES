import sys

# Accept marks from command line arguments
# Example: python marks_grade.py 85 76 90 88 95
if len(sys.argv) != 6:
    print("Please provide marks of 5 subjects as command line arguments.")
    sys.exit()

# Convert all arguments (strings) to integers
marks = [int(arg) for arg in sys.argv[1:6]]

# Calculate average
average = sum(marks) / len(marks)

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

# Print results
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")