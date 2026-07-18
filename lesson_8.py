
######## for while ########

# index elements: list, str, tuple, set, dict

# range()

# my_list = [1, 2, 3]
#
# for index in my_list:
#     print(index)
#     my_list.append(1)


# for index in range(len(my_list)):
#     print(my_list[index])
#     my_list.append(1)



# 1.
# my_list = [0, 1, 12, 1, 1]
# new_list = []
# what_we_want_to_find = 0
#
# if what_we_want_to_find in my_list:
#     for new in my_list:
#         if new == what_we_want_to_find:
#             continue
#         new_list.append(new)
#
#     number_of_iterations = my_list.count(what_we_want_to_find)
#     for _ in range(number_of_iterations):    # _ заглушка для змінних які ніде не використовуються
#         new_list.append(what_we_want_to_find)
#
#     print(new_list)
# else:
#     print("Zero not found")




# 2.
# my_list = [0, 1, 0, 0, 12, 1, 1]
# new_list = []
# what_we_want_to_find = 0
#
# if what_we_want_to_find in my_list:
#     number_of_iterations = my_list.count(what_we_want_to_find)
#
#     for index in range(len(my_list)):
#         if my_list[index] != what_we_want_to_find:
#             new_list.append(my_list[index])
#
#     list_with_zeros = [0] * number_of_iterations
#     new_list.extend(list_with_zeros)
#
#     print(new_list)
# else:
#     print("Zero not found")




# 3.
# my_list = [0, 1, 0, 0, 12, 1, 1]
# what_we_want_to_find = 0
#
# if what_we_want_to_find in my_list:
#
#     for index in range(len(my_list) - 1, -1, -1):
#         if my_list[index] == what_we_want_to_find:
#             my_list.append(my_list.pop(index))
#
# else:
#     print("Zero not found")
#
# print(my_list)




# 4.

# my_list = [0, 1, 0, 6, 0, 9, 0, 0, 7, 8]
# what_we_want_to_find = 0
#
# if what_we_want_to_find in my_list:
#     number_of_iterations = my_list.count(what_we_want_to_find)
#
#     # for index in range(len(my_list)):
#     for _ in range(number_of_iterations):
#         # if my_list[index] == what_we_want_to_find:
#         my_list.remove(what_we_want_to_find)
#         my_list.append(what_we_want_to_find)
#
# else:
#     print("Zero not found")
#
# print(my_list)











# 5.
# my_list = [0, 1, 0, 1, 1, 1, 0, 6, 0, 9, 0, 0, 7, 8]
#
# my_list.sort(reverse=True, key=bool)  #lambda func
#
# print(my_list)









# 6.

# my_list = [1, 0, 5, 6, 7, 0]
#
# index = 0
#
# for i in range(len(my_list)):
#     if my_list[i] != 0:
#         my_list[i], my_list[index] = my_list[index], my_list[i]
#         index += 1
#
# print(my_list[99])


# while for 4th.

my_list = [1, 0, 5, 6, 7, 0, 9]
what_we_want_to_find = 0
number_of_iterations = my_list.count(what_we_want_to_find)

new_list = []
index = 0

while index < number_of_iterations:

    my_list.remove(what_we_want_to_find)
    my_list.append(what_we_want_to_find)

    index += 1

print(my_list)

# for _ in range(number_of_iterations):
#
#
#     my_list.remove(what_we_want_to_find)
#     my_list.append(what_we_want_to_find)








