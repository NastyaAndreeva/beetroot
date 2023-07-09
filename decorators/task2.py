def stop_words(words: list):
    def wrapper_func(func):
        def inner_wrapper(name):
            result:str = func(name)
            for word in words:
                if word in result:
                    new_string = result.replace(word, "*")
                    result = new_string
            return new_string
        return inner_wrapper
    return wrapper_func

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Steve") == "Steve drinks * in his brand new *!")
print(create_slogan("Steve"))