import asyncio

async def calculate_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

async def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result

async def calculate_squares(n):
    return n * n

async def calculate_cubic(n):
    return n **3

async def main():
    numbers = list(range(1, 11))
    fibonacci_results = await asyncio.gather(*(calculate_fibonacci(n) for n in numbers))
    factorial_results = await asyncio.gather(*(calculate_factorial(n) for n in numbers))
    squares_results = await asyncio.gather(*(calculate_squares(n) for n in numbers))
    cubic_results = await asyncio.gather(*(calculate_cubic(n) for n in numbers))
    return fibonacci_results, factorial_results, squares_results, cubic_results

if __name__ == '__main__':
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    fib, fact, sq, cub = loop.run_until_complete(main())
    end_time = time.time()
    print("Asyncio Results:")
    print("Fibonacci:", fib)
    print("Factorial:", fact)
    print("Squares:", sq)
    print("Cubic:", cub)
    print(f"Execution time: {end_time - start_time} seconds")

 