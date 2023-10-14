import multiprocessing

def calculate_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_squares(n):
    return n * n

def calculate_cubic(n):
    return n ** 3

def main():
    numbers = list(range(1, 11))
    with multiprocessing.Pool() as pool:
        fibonacci_results = pool.map(calculate_fibonacci, numbers)
        factorial_results = pool.map(calculate_factorial, numbers)
        squares_results = pool.map(calculate_squares, numbers)
        cubic_results = pool.map(calculate_cubic, numbers)
    return fibonacci_results, factorial_results, squares_results, cubic_results

if __name__ == '__main__':
    import time
    start_time = time.time()
    fib, fact, sq, cub = main()
    end_time = time.time()
    print("Multiprocessing:")
    print("Fibonacci:", fib)
    print("Factorial:", fact)
    print("Squares:", sq)
    print("Cubic:", cub)
    print(f"Execution time: {end_time - start_time} seconds")
