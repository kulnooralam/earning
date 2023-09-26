def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return (n * (n + 1)) // 2

try:
    N = int(input("Enter a positive integer N: "))
    
    if N <= 0:
        print("Please enter a positive integer.")
    else:
        result = sum_of_natural_numbers(N)
        print(f"The sum of the first {N} natural numbers is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
