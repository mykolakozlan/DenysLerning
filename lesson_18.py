

# def my_add(num_1):
#     return num_1 + 2
#
#
# def my_mul(num_1):
#     return num_1 * 2
#
#
#
# list_of_funcs = [my_add, my_mul]
#
# value_1 = 1
# value_2 = 2
#
#
# for my_func in list_of_funcs:
#     print(my_func(value_1, value_2))


# def change_num(number, func):
#     return func(number)
#
# print(change_num(3, lambda x: x + 5))


# map()
# my_list = [1, 2, 3]
# squares = list(map(lambda x: x ** 2, my_list))
# print(squares)
#
#
# # filter()
#
# numbers = [1, 2, 3, 4]
# even = list(filter(lambda x: x % 2 == 0, numbers))
# print(even)



# zip()

# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = ["red", "apple", "gold", "good"]
# my_list_3 = [True, False, None]
#
#
# # for value in zip(my_list_1, my_list_2, my_list_3):
# #     print(value)
#
#
# for index in range(len(my_list_3)):
#     print((my_list_1[index], my_list_2[index], my_list_3[index]))




######## runtime ############

# status = 5
#
# if status == 1:
#
#
#     def my_func(num_1):
#         return num_1 + 2
#
#
#     print(my_func(status))
# else:
#
#
#     def my_func(num_1):
#         return num_1 * 2
#
#
#     print(my_func(status))



################## Рекурсія ##################


# def fibo(n):
#     a = 0
#     b = 1
#
#     for i in range(2, n + 1):
#         a, b = b, a + b
#
#     return b
#
# 0, 1,
# 1, 1,
# 1, 2,
# 2, 3
# 3, 5
# 5, 8


# def fibo(n):
#     print(n)
#     if n in (1, 2):
#         result = 1
#     else:
#         result = fibo(n - 1) + fibo(n - 2)
#
#     return result
# #
# # 4 fibo(3), fibo(2)X
# # 3 fibo(2), fibo(1)
# # 2 -> 1
# # 1
# # 2
# # 3
# #
# print(fibo(4))



#################### Generators ####################

import sys

# gen = range(1, 5000000000)
# print(gen)
#
# print(sys.getsizeof(gen))


# def add_one(num):
#     return num + 1
#
#
# def count(start, func):
#     while True:
#         yield start
#         start = func(start)
#
#
# counter = count(1, add_one)
#
# print(counter)
# print(next(counter)) #0
# print(next(counter)) #1
#
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))












