import time

class CustomException(Exception):
    def __init__(self, msg):
        with open("logs.txt", "w") as file:
            file.write(msg)

custom_exception = CustomException("There is my custom exception: " + time.strftime("%Y-%m-%d %H:%M:%S"))
