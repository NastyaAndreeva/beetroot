class User:
    def __init__(self, email):
        if User.validate(email):
            self.email = email
        else:
            self.email = "test@gmail.com"

    def __str__(self):
        return self.email

    @classmethod
    def validate(self, email):
        if "@" in email:
            print(f"{email} is valid")
            return True
        else:
            print(f"{email} is invalid")
            return False

user_1 = User("andreeva@gmail.com")
user_2 = User("blue-lock.com")

print(user_1)
print(user_2)