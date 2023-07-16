def is_pangram(s):
    test_string = "abcdefghijklmnopqrstuvwxyz"
    symb_string = ".,':; "
    symb_list = sorted(s.lower())
    new_str = ""
    for el in symb_list:
        if not el.lower() in new_str and el.isalnum() and not el.isnumeric():
            new_str += el.lower()
    if test_string == new_str:
        return True
    return False


# print(is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'))
# my_set = set("abcdefghijklmnopqrstuvwxyz")
# new_set = set('The quick brown fox jumps over the lazy dog.'.lower())
# print(my_set.issubset(new_set))

def is_pangram_2(s):
    my_set = set("abcdefghijklmnopqrstuvwxyz")
    new_set = set(s.lower())
    return True if my_set.issubset(new_set) else False

print(is_pangram_2('The quick brown fox jumps over the lazy dog.'))

class Person:
    my_var = 2
    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def my_method():
        print(Person.my_var)

person = Person("Rin")
person.my_method()