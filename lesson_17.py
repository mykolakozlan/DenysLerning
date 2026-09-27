

# def add_one(some_list):
#     new = ""
#
#     for some in some_list:
#         new += str(some)
#
#     some_string = str(int(new) + 1)
#
#     return [int(y) for y in some_string]
#
# result = add_one([1, 2, 3, 4, 5])
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")


##### metod 2 ######

# def add_one(some_list):
#
#     new_list = [str(number) for number in some_list]
#     new_string = str(int("".join(new_list)) + 1)
#
#     return  [int(x) for x in new_string]
# #
# print(add_one([1, 2, 3, 4]))
# #
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")



import string

#
# def is_palindrome(string_1):
#     new_string = ""
#
#
#     for x in string_1:
#         if x.isalpha() or x.isdigit():
#             y = x.lower()
#             new_string += y
#
#
#     new_1 = new_string[::-1]
#
#     if new_string == new_1:
#         return  True
#
#     return False
#
#
# print(is_palindrome("A man, a plan, a canal: Panama"))
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
#
#
# print("ОК")






####### metod 1 #######


# def find_unique_value(n):
#     from decimal import Decimal
#
#     n = [value_1 for value_1 in n if isinstance(value_1, (int, float, Decimal))]
#
#     for value_2 in set(n):
#         summ_value = n.count(value_2)
#         if summ_value == 1:
#             return value_2
#
#
# result = find_unique_value([1, 2, 1, 1, "Hello", [1, 2, 3]])
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")


####### metod 2 #######

#
# def find_unique_value(n):
#
#     for value in n:
#         summ_value = n.count(value)
#         if summ_value == 1:
#          return value
#
# result = find_unique_value([1, 2, 1, 1])
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")





# def some_func(num_1, num_2):
#     return num_1 + num_2
#
#
# args = 1, 2
#
# print(some_func(*args))


# lambda # анонімна функція

# square = lambda x: x * x
#
# # def square(x):
# #     return x * x
#
#
# result_1 = square(5)
#
# print(result_1)


# some_list = [1, 2, 3, 0, 0]
#
# some_list.sort(key=bool, reverse=True)
# sorted(some_list, key=bool, reverse=True)



# map filter

# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)


numbers = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)





























