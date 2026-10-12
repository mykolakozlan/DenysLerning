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

# def some_gen():
#     yield 54
#
# gen = some_gen()
# print(gen)
# print(next(gen))
# print(next(gen))

# def s_gen():
#     x = 1
#     while x > 0:
#         x = yield 45
#
#         print(f"Receiving {x}")
#         if x is None:
#             x = 0
#
# new_val = s_gen()
# print(next(new_val))
# new_val.send(90)
# print(next(new_val))


# value_list = [i * 2 for i in range(5)]
# print(value_list)


# value_list = (i * 2 for i in range(5))
# print(value_list)
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))



# iter()

# Gen Speed

import time
#
# a = []
# start = time.time()
# for i in range(10_000_000):
#     a.append(i ** 2)
# end = time.time()
# print("for cicle t = ", end-start, " s")
#
# start = time.time()
# b = [i ** 2 for i in range(10_000_000)]
# end = time.time()
# print("for generator list t = ", end-start, " s")
# #
# start = time.time()
# c = (i ** 2 for i in range(10_000_000))
# end = time.time()
# print("for generator t = ", end-start, " s")
#
# start = time.time()
# c = list(c)
# end = time.time()
# print("for generator to list t = ", end-start, " s")

