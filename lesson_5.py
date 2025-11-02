
# my_input = int(input("Enter your number:"))                #1234
#
# thousands, left_1 = divmod(my_input, 1000)                 # (1, 234)
# hundreds, left_2 = divmod(left_1, 100)                  # (2, 34)
# tens, ones = divmod(left_2, 10)                         # (3, 4)
#
# print(ones, tens, hundreds, thousands,  sep='')


# print([100, 0])
# a, d4 = ["Hello", "bye"]
# print(a)
# print(d4)

# my_list = ["Hello", "bye", 1, 2, 3, 4]
#
# a, d4, d5, *tmp = my_list
# print(a)
# print(d4)
# print(d5)
# print(tmp)

# glass_1, glass_2 = "water", "milk"
#
# print(glass_1, glass_2)
#
# glass_1, glass_2 = glass_2, glass_1
#
# print(glass_1, glass_2)

#################### List ########################


# value_list = list()
# value_list = [3, 1.2, "hello", True, None, [1, 2, 3]]

# my_list = [1, 2, 3, 4, 5, 6] # index from 0 to ...

# print(value_list)
# print(my_list[0]) № перший елемент ліста
# print(my_list[-1]) # перше з кінця
# print(my_list[10])
# print(my_list[0:3]) # від початку і до третього індексу(виключно)
# print(my_list[:3]) # від початку і до третього індексу(виключно)
# print(my_list[3:]) # від третього індексу і до кінця
# print(my_list[10:55]) # видає пустий ліст бо індеки не заповнені
# print(my_list[1:6:2]) # третє значення це крок

# print(my_list[::-1]) # перевертає ліст(реверс)


# base_list = [1, 2, 3]
#
# my_new_list = base_list * 4
#
# # print(my_new_list)
#
# base_list[0] = "hello"
#
# print(f'base_list = {base_list}')
# print(f'my_new_list = {my_new_list}')

# from copy import deepcopy
#
#
# base_list = [1, 2, 3, [True, False]]
#
# # my_new_list = [base_list] * 4
# my_new_list = [base_list.copy()] * 4
# my_new_list = [deepcopy(base_list)] * 4
#
# # my_new_list = [link, link, link, link]
# # base_list.copy() = [1, 2, 3, link]
#
# # print(my_new_list)
# print(f'before my_new_list = {my_new_list}')
#
# base_list[-1][0] = "hello"
#
# print(f'base_list = {base_list}')
# print(f'my_new_list = {my_new_list}')

# my_list = [1, 2, 3]
#
# my_list[0] = "hello"
#
# print(my_list)
