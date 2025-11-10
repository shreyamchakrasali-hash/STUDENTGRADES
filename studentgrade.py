import sys

def calculate_average_and_grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5

    # Determine grade based on average
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

# Check if user provided exactly 5 marks
if len(sys.argv) != 6:
    print("Usage: python program.py <mark1> <mark2> <mark3> <mark4> <mark5>")
    sys.exit(1)

# Convert command-line arguments to floats
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
m3 = float(sys.argv[3])
m4 = float(sys.argv[4])
m5 = float(sys.argv[5])

# Function call
calculate_average_and_grade(m1, m2, m3, m4, m5)