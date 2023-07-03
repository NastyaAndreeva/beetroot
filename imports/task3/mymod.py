def count_lines(name):
    with open(name, 'r') as file:
        return len(file.readlines())

    
def count_chars(name):
    with open(name, 'r') as file:
        return len(file.read())

def test(name):
    print(count_lines(name))
    print(count_chars(name))