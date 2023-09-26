def print_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    
    return factors

try:
    num = int(input("Enter a number: "))
    
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        result = print_factors(num)
        print(f"The factors of {num} are: {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
