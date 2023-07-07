with open("myfile.txt", "w") as file:
    file.write("Welcome to hell")

try:
    with open("myfile1.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("The file path is incorrect")