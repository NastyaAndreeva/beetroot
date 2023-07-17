class Mathematician:

    @staticmethod
    def square_nums(list_of_int):
        return [x**2 for x in list_of_int]

    @staticmethod
    def remove_positives(list_of_int):
        return [x for x in list_of_int if x < 0]

    @staticmethod
    def filter_leaps(list_of_dates):
        return [year for year in list_of_dates if not year % 4]
 
m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))