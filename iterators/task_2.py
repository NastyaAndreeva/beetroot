def in_range(start, end, optional_step = 1):
    while start <= end:
        yield start
        start += optional_step

for item in in_range(10, 25):
    print(item)