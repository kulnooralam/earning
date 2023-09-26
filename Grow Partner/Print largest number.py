def find_largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    largest_number = find_largest_number(num1, num2, num3)
    print(f"The largest number is {largest_number}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
