# def prime_generator(value):
#
#     for x in range(1, (value + 1)):
#         result = []
#
#         for y in range(1, value + 1):
#             if x % y == 0:
#                 result.append(y)
#         if len(result) == 2:
#             yield x
#
#
# from inspect import isgenerator
#
# gen = prime_generator(10)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')
#














# def simple_num(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def simple_num(num):
#     div = 1
#     div_list = []
#     while div <= num:
#         if num % div == 0:
#             div_list.append(div)
#         div += 1
#
#     return True if len(div_list) == 2 else False
#
#
# def prime_generator(end):
#     number = 1
#     while number <= end:
#         if simple_num(number):
#             yield number
#         number += 1
#
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')


























##### option 1 ######

# def is_even(value):
#
#     if not str(value).strip("-").isdigit():
#
#         return "Sorry, the value is not a digit"
#
#     if (str(value).endswith("0")
#         or str(value).endswith("2")
#         or str(value).endswith("4")
#         or str(value).endswith("6")
#         or str(value).endswith("8")):
#
#         return True
#
#     else:
#
#         return  False
#
# print(is_even(5689))
#
# assert is_even(2) == True, 'Test1'
#
# assert is_even(5) == False, 'Test2'
#
# assert is_even(0) == True, 'Test3'
#
# print('OK')

# #### option 2 #####
#
# def is_even(value):
#
#     if not str(value).strip("-").isdigit():
#
#         return "Sorry, the value is not a digit"
#
#     if (str(value)[-1] == "0"
#         or str(value)[-1] == "2"
#         or str(value)[-1] == "4"
#         or str(value)[-1] == "6"
#         or str(value)[-1] == "8"):
#
#         return True
#
#     else:
#
#         return  False
#
# print(is_even(5689))
#
# assert is_even(2) == True, 'Test1'
#
# assert is_even(5) == False, 'Test2'
#
# assert is_even(0) == True, 'Test3'
#
# print('OK')

#### option 3 ####

# def is_even(value):
#
#     if not str(value).strip("-").isdigit():
#         return "Sorry, the value is not a digit"
#
#     # if str(value)[-1] in "02468":
#     if str(value)[-1] in ("0", "2", "4", "6", "8"):
#         return True
#     else:
#         return  False
#
# print(is_even(5689))
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
#
# print('OK')





# def is_even(number):
#     res = False
#     list_num = str(number)
#
#     # if list_num[-1] in ('0', '2', '4', '6', '8'):
#     if list_num[-1] in '02468':
#         res = True
#
#     return res


# def is_even(number):
#     return (number & 1) == 0
#
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print('Ok')


# write
# writelines

filename = "test.txt"

# my_file = open(filename, "w")
#
# my_file.write("Hello World!")
# my_file.write("Hello World!")
# my_file.write("Hello World!")
# my_file.write("Hello World!")
# my_file.write("Hello World!")
# my_file.write("Hello World!")
#
# my_file.close()


# with open(filename, "w") as my_file:
#     my_file.write("Hello Worldddddd!\n")
#     my_file.write("Hello Worl3333d!")


# my_list = ["red", "green", "white"]
#
# my_file = open(filename, "w")
#
# for i in my_list:
#     my_file.writelines(i + "4444\n")
#
# # my_file.writelines(my_list)
#
# my_file.close()


# read
# readlines
# readline

# my_file = open(filename, "r")
#
# # data = my_file.read()
# # data = my_file.readlines()
# # data = my_file.readline()
#
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
#
# my_file.close()


# with open(filename, "r") as my_file:
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())


# with open(filename, "a+") as my_file:
#     data = my_file.write("gggggggg!\n")
#     my_file.seek(3)
#     context = my_file.read()
#     print(context)


# with open(filename, "wt", encoding="UTF-8") as my_file:
#     my_file.write("gggggggg!\n")


################################## OOP ################################


# class MyCar(object):
#     pass


# class MyCar:
#     color = "red"                    # атрибут класу
#     engine = 2000
#     body = "sedan"
#
# car_1 = MyCar()                 #екземпляр класу
# car_2 = MyCar()                 #екземпляр класу
#
# car_1.sticker = "Тачка на прокачку"            #атрибуи екземпляру класу
#
# print(car_1.engine)
#
# car_1.engine = 2400
#
# print(car_1.engine)
# print(car_2.engine)

# my_str = "hello"
# str
#
# print(type(my_str))



















