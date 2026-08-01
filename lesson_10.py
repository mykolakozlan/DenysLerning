# ДЗ 3 Список із 3 елементів
#
# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
#
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
#
# Приклад:
#
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]
from curses.ascii import isalpha

# my_list = ['fff', 3, '7675', 7,5, 9, 'llll', 10]
#
# new_list = []
#
# new_list = [my_list[0], my_list[2], my_list[-2]]
#
# print(new_list)

# value_str = "hello"
#
# # next()
#
# for sym in value_str:
#     print(value_str)

# value_str = "hello"
# # # value_str = [1, 2, 3, 4]
# #
# # # for sym in range(len(value_str)):
# # #     print(sym, value_str[sym])
# #
# #
# # # # enumerate()
#
# index_l = None
#
# # for index, sym in enumerate(value_str):
# for sym in enumerate(value_str):
#     print(sym)
#     # print(index, sym)
# #
# # print("end")
# print(sym)


######### String #######

# value_str = "helloooooool"

# find()

# print(value_str.find("l"))
# print(value_str.rfind("l"))


# first_num = "klcmlkwemakl73q0,msnw920"
#
# real_first_num = [73, 0, 920]
# count = 0

# isspace()
# isalpha()
# isdigit()
# print(first_num.isdigit())

# for symbol in first_num:
#     if symbol.isdigit():
#         real_first_num += symbol
#     # else:
#     #     count += 1
#     #     # print(symbol)
# print(real_first_num)
# print(count)


# value_str = "helloooooool"
# value_find = value_str.find("l", 4, 7)
# # value_index = value_str.index("2")
#
# print(value_find)
# print(value_index)

# find()
# index()


# split join

# file_address = "C:/My compu.ter/Some f.older/count+user_identifier+type.png"
# file_address = "C:/My compu.ter/Some f.older/3_ID-4531_2.png"
#
# value_split = file_address.rsplit(".", 1)
# print(value_split)
#
# value_split[-1] = "jpeg"
# value_join = ".".join(value_split)
# print(file_address)
# print(value_join)


# startswith endswith

# value_str = "hello"
#
# # value_startswith = value_str.startswith("he")
# value_endswith = value_str.endswith("lo")
# # print(value_startswith)
# print(value_endswith)

# "jkfjeklj88320kjnk"
# "xe/:u9jkfjeklj88320kjnk"
# "xe/:u9fsrfrs6876ik"
# "xe/:u9fseffr6642k"
# "xe/:u9dwedcsrs42k"


# name = "Nick"
#
# value_string = f"Hi, my name is {name}"
# value_format = "Hi, my name is {}, {}".format(name, 5)
#
# print(value_format)

# name = "______Nick______"
#
# value_strip = name.strip("_")
# value_rstrip = name.rstrip("_")
# value_lstrip = name.lstrip("_")
# print(name)
# print(value_strip)
# print(value_rstrip)
# print(value_lstrip)


############ ASCII ###############

# value = "kfl;dsklfelfem;l"
# print(ord(value))
# print(chr(105))



















