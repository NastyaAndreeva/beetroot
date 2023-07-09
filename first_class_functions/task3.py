def choose_func(nums_list, cb1, cb2):
    for el in nums_list:
        if el < 0:
            return cb2(nums_list)
    return cb1(nums_list)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
print(choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25])
print(choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5])
