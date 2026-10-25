#
#
# def pow(x):
#     return x ** 2
#
#
# def some_gen(begin, end, func):
#     for x in range(end):
#         yield begin
#         begin = func(begin)
#
#
# from inspect import isgenerator
#
#
# gen = some_gen(2, 4, pow)
#
# # print(next(gen))
# # print(next(gen))
# # print(list(gen)) # [] -> [16] -> [16,256] -> Func next Error!!! return [16,256]
# # print(list(gen)) # [] -> Func next Error!!! return []
#
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
#
# print('OK')
from os import write

#### option 1 ######
# def letters_and_spaces(txt):
#     first_text = ""
#
#     for value in txt:
#         if value.isalpha() or value == "'" or value.isspace():
#             first_text += value
#         else:
#             first_text += " "
#
#     return first_text
#
#
# def list_without_spaces(some_txt):
#     new_text = some_txt.strip().split()
#     return new_text[0]
#
#
# # LEGB
#
#
# def first_word(text):
#     rslt = letters_and_spaces(text)
#     return list_without_spaces(rslt)


# import re
#
#
# def first_word(text):
#
#     match = re.search(r"[a-zA-Z']+", text)
#
#     if match:
#         return match.group(0)
#
#     return ""
#
#
# print(first_word( " ,. 2 don't. tuch  "))
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'


# ##### option 1 ######
#
# def is_even(value):
#     return value % 2 == 0
#
# print(is_even(4))
#
# assert is_even(2) == True, 'Test1'
#
# assert is_even(5) == False, 'Test2'
#
# assert is_even(0) == True, 'Test3'
#
# print('OK')
#
# ## option 2 #####
#
# def is_even(value):
#
#     if not str(value).strip("-").isdigit():
#         return "Sorry, the value is not a digit"
#     else:
#         # return True if value % 2 == 0 else False
#         return value % 2 == 0
#
# print(is_even(-4))
#
# assert is_even(2) == True, 'Test1'
#
# assert is_even(5) == False, 'Test2'
#
# assert is_even(0) == True, 'Test3'
#
# print('OK')

##### option 3 ######


# def start_is_even(value):
#     return int(value) % 2 == 0
#
#
# def check_at_int(value):
#     if not str(value).strip("-").isdigit():
#         return "Sorry, the value is not a digit"
#     else:
#         return start_is_even(value)
#
#
# def is_even(value):
#     return check_at_int(value)
#
#
# print(is_even("4"))
#
# assert is_even(2) == True, 'Test1'
#
# assert is_even(5) == False, 'Test2'
#
# assert is_even(0) == True, 'Test3'
#
# print('OK')



# [1, 2, 3, 4, 5]



############################################ Files ###################################################################

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


with open(filename, "w") as my_file:
    my_file.write("Hello World!\n")
    my_file.write("Hello World!")














































