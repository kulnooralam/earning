def generate_fibonacci_series(n):
    fibonacci_series = []
    if n <= 0:
        return fibonacci_series
    elif n == 1:
        fibonacci_series.append(0)
    elif n == 2:
        fibonacci_series.extend([0, 1])
    else:
        fibonacci_series.extend([0, 1])
        for i in range(2, n):
            next_term = fibonacci_series[i - 1] + fibonacci_series[i - 2]
            fibonacci_series.append(next_term)
    return fibonacci_series

try:
    N = int(input("Enter the number of terms in the Fibonacci series (N): "))
    
    if N <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_series = generate_fibonacci_series(N)
        print(f"The first {N} terms of the Fibonacci series are:")
        for term in fibonacci_series:
            print(term, end=" ")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
