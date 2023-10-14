def with_index(iterable, start=0):
    for item in iterable:
        yield (item, start)
        start += 1

for item in with_index([4, 5, 6, 7, 8]):
    print(item)
