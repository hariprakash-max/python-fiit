def fibonacci(n):
    fib_series = [0, 1]

    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series


# Example: Generate Fibonacci series up to the 10th term
n = 10
result = fibonacci(n)

print(f"Fibonacci series up to {n} terms: {result}")
