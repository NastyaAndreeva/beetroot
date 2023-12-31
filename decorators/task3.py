def arg_rules(type_: type, max_length: int, contains: list):
    def outer_wrapper(func):
        def inner_wrapper(name):
            if not type(name) == type_:
                return f"{name} must be a string"
            if len(name) > max_length:
                return "The name is too long"
            for el in contains:
                if not el in name:
                    return f"{name} must contain {el}"
            return func(name)
        return inner_wrapper
    return outer_wrapper

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan(4))
print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('joh05gmail.com'))
print(create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!')