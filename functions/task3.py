def make_operation(operation, *numbers):
    numbers = list(numbers)
    result = numbers[0]
    if operation == '+':
        for idx in range(1, len(numbers)):
            result += numbers[idx]
    elif operation == '-':
        for idx in range(1, len(numbers)):
            result -= numbers[idx]
    else:
        for idx in range(1, len(numbers)):
            result *= numbers[idx]
    return result

print(make_operation("*", 5, 5, -10, -20))