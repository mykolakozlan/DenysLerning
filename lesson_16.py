



# def correct_sentence(text):
#     new_text = text[0].upper() + text[1:]
#     if new_text[-1] != ".":
#         # new_text_2 = f"{new_text}."
#         # new_text_2 = new_text + "."
#
#         # new_text += "."
#         return new_text
#     else:
#         return new_text
#
# # result = correct_sentence("hello. hriends")
# # print(result)
#
#
# assert correct_sentence("hello, friends.") == "Hello, friends.", "Test1"
# assert correct_sentence("hello") == "Hello.", "Test2"
# assert correct_sentence("Hello. Friends") == "Hello. Friends.", "Test3"
# assert correct_sentence("Hello, friends.") == "Hello, friends.", "Test4"
# assert correct_sentence("hello, friends.") == "Hello, friends.", "Test5"
# #
# print("OK")



# def correct_sentence(text):
#     text = text.strip()
#
#     if text[0].islower():
#         text = text[0].upper() + text[1:]
#         # text = text.capitalize()
#
#     # if text[-1] != '.':
#     if not text.endswith("."):
#         text += "."
#
#     return text
#
# assert correct_sentence("Greetings, friends") == "Greetings, friends.", 'correct_sentence error: check for dot'
# assert correct_sentence("hello.") == "Hello.", 'correct_sentence error: check for capital letter'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')



# def second_index(text, some_str):
#     first_index = text.find(some_str)
#     target_index = text.find(some_str, first_index + 1)
#     if target_index == -1:
#         return  None
#
#     return  target_index
#
#
# (second_index("Hello, hello", "lo"))
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
#
# print('ОК')




# def second_index(text: str, some_str: str) -> str:
#     first_index = text.find(some_str)
#
#     if first_index == -1:
#         return None
#
#     seconds_index = text.find(some_str, first_index + 1)
#
#     if seconds_index == -1:
#         return None
#
#     return seconds_index
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')




#### 1 ####

# def common_elements(num_1, num_2):
#     list_1 = []
#     list_2 = []
#
#     for value_1 in range(num_1):
#         if value_1 % 3 == 0:
#             list_1.append(value_1)
#     set_1 = set(list_1)
#
#     for value_2 in range(num_2):
#         if value_2 % 5 == 0:
#             list_2.append(value_2)
#     set_2 = set(list_2)
#
#     result = set_1.intersection(set_2)
#
#     return result
#
# assert common_elements(100, 100) == {0, 75, 45, 15, 90, 60, 30}
# print("OK")




####### 2 #######

# def find_common(n_1, n_2):
#     result_1 = set(n_1)
#     result_2 = set(n_2)
#     result = result_1.intersection(result_2)
#     return result
#
#
# def common_elements(num_1, num_2):
#     # """This function is nested inside another function."""
#
#     list_1 = []
#     list_2 = []
#
#     for value_1 in range(num_1):
#         if value_1 % 3 == 0:
#             list_1.append(value_1)
#
#     for value_2 in range(num_2):
#         if value_2 % 5 == 0:
#             list_2.append(value_2)
#
#
#     return find_common(list_1, list_2)
#
# print(common_elements(100,100))
#
#
# assert common_elements(100, 100) == {0, 75, 45, 15, 90, 60, 30}
# print("OK")


# def common_elements():
#     multiples_of_3 = [num for num in range(100) if num % 3 == 0]
#     multiples_of_5 = [num for num in range(100) if num % 5 == 0]
#
#
#     return set(multiples_of_3).intersection(set(multiples_of_5))


# def common_elements():
#     multiples_of_3 = {num for num in range(0, 100, 3)}
#     multiples_of_5 = {num for num in range(0, 100, 5)}
#
#     return multiples_of_3 & multiples_of_5   # побітові операції в пайтон


#
# IS_EMAIL_CONFIRMED = True
#
#
# def add_func(num_1, num_2, is_conf):
#     """This is doing something important!!!!!"""
#     result = 0
#
#     if is_conf:
#         result = num_1 + num_2
#
#     return result
#
#
# print(add_func(is_conf=IS_EMAIL_CONFIRMED, num_2=10, num_1=5)) # іменований виклик
# print(add_func(10, num_2=5, is_conf=IS_EMAIL_CONFIRMED)) # змішаний виклик


# import operator
#
#
# actions = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv,
# }
#
# num_1 = float(input("num_1 "))
# symbol = input("symbol ")
# num_2 = float(input("num_2 "))
#
# # my_func = actions[symbol]
# my_func = actions.get(symbol)
#
# if my_func:
#     print(my_func(num_1, num_2))
# else:
#     print("ERROR")


############### L(local) E(enclosing) G(global) B(built-in) ###############


# IS_EMAIL_CONFIRMED = True
#
#
# def add_func(num_1: int, num_2: int, is_conf: bool=False) -> int:
#     """This is doing something important!!!!!"""
#     result = 0
#
#     if is_conf:
#         result = num_1 + num_2
#
#     return result
#
#
# # print(add_func(is_conf=IS_EMAIL_CONFIRMED, num_2=10, num_1=5)) # іменований виклик
# # print(add_func(10, num_2=5, is_conf=IS_EMAIL_CONFIRMED)) # змішаний виклик
#
# result = add_func("2","3", IS_EMAIL_CONFIRMED)
#
# print(result, type(result))



############## args kwargs ##################


# print(1, 2)


# num_1, num_2, *tmp = (1, 2)
#
# print(tmp)



# def create_list(*args):
#     result = []
#
#     print(args)
#     print(type(args))
#
#     if args:
#         result = list(args)
#
#     return result
#
#
# print(create_list(1, 3, 4, 5))


# def teacher_and_his_group(teacher, *group):
#     dict = {
#         "teacher": teacher,
#         "students": list(group)
#     }
#
#     return dict
#
#
# print(teacher_and_his_group("Nick", "Sasha", "Petro", "Petro"))



# **kwargs


# def add_func(num_1, num_2, **kwargs):
#     """This is doing something important!!!!!"""
#     result = 0
#
#     print(kwargs)
#     print(type(kwargs))
#
#     if kwargs.get("is_conf"):
#         result = num_1 + num_2
#
#     if kwargs.get("name"):
#         print(f"I'm {kwargs.get("name")}")
#
#     if kwargs.get("age"):
#         print(f"I'm {kwargs.get("age")}")
#
#     return result
#
# print(add_func(1, 2, is_conf=True,
#                                    name="Nick",
#                                    age=19))

# from lesson_15 import get_weather
#
# print(get_weather(15, "cloudy"))





