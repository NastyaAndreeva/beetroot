def binary_search_recursive(arr, element, left, right):
    if left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            return binary_search_recursive(arr, element, mid + 1, right)
        else:
            return binary_search_recursive(arr, element, left, mid - 1)
    else:
        # The element wasn't found
        return -1

def fibonacci_search(arr, element):
    def fibonacci(n):
        if n <= 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            fib = [0, 1]
            while len(fib) < n + 1:
                fib.append(fib[-1] + fib[-2])
            return fib

    def find_index(arr, element, left, offset, fib):
        if left >= len(arr) or element < arr[left]:
            return -1

        while left < len(arr):
            if arr[left] == element:
                return left
            if left == offset:
                return -1
            left += 1
        return -1

    n = len(arr)
    fib = fibonacci(n)
    offset = -1

    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    while fib:
        index = min(offset + fib[-2], n - 1)
        if arr[index] < element:
            fib = fib[:-1]
            offset = index
        elif arr[index] > element:
            fib = fib[:-2]
        else:
            return index
    # The element wasn't found
    return -1

