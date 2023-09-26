def calculate_grade(percentage):
    if percentage >= 80:
        return "Grade A"
    elif percentage >= 60:
        return "Grade B"
    elif percentage >= 40:
        return "Grade C"
    else:
        return "Grade D"

try:
    subject1 = float(input("Enter marks obtained in subject 1: "))
    subject2 = float(input("Enter marks obtained in subject 2: "))
    subject3 = float(input("Enter marks obtained in subject 3: "))
    
    total_marks = subject1 + subject2 + subject3
    percentage = (total_marks / 300) * 100
    
    grade = calculate_grade(percentage)
    
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
except ValueError:
    print("Invalid input. Please enter valid marks as numbers.")
