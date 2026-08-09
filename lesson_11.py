# import string
# import keyword
#
# name = input(str("Enter the variable name:"))
# result = True
#
# if name[0].isdigit():
#     result = False
# for letter in name:
#     if letter.isupper():
#         result = False
# if name in keyword.kwlist:
#     result = False
# for old_name in name:
#     if old_name in string.punctuation and old_name != "_":
#         result = False
# for young_name in name:
#     if young_name.isspace():
#         result = False
#
# print(result)


import keyword
import string

# name_var = input("Please enter a name of variable: ")
# result = ""
#
# if name_var:
#     result = "True"
#
#     if name_var[0].isdigit():
#         result = "False"
#     elif keyword.iskeyword(name_var):
#         result = "False"
#     else:
#         for symbol_str in range(len(name_var)):
#         # for symbol_str in name_var:
#             if name_var[symbol_str].isupper():
#                 result = "False"
#             elif name_var[symbol_str].isspace():
#                 result = "False"
#             elif name_var[symbol_str] in string.punctuation and name_var[symbol_str] != "_":
#                 result = "False"
#             elif name_var[symbol_str] == "_":
#                 if symbol_str > 0 and name_var[symbol_str] == name_var[symbol_str-1]:
#                     result = "False"
#
# else:
#     result = "empty string"
#
#
# print(f'Name of variable "{name_var}" is {result}')




# my_string = input("Please enter your variable: ")
# result = False
#
# if my_string.isidentifier():
#     if my_string == "_" or my_string.islower():
#         result = True
#
#
# print(result)




# import string
#
# # 'Python Community' -> #PythonCommunity
# # 'i like python community!' -> #ILikePythonCommunity
# # 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
#
# first_adress = input(str("Enter the variable name:"))
#
# result = ""
# hashtag = '#'
# new_result = []
#
# # if len(first_adress) > 500:
# #     first_adress = first_adress[:500]
#
# for x in first_adress:
#     if x not in string.punctuation:
#         result += x
#
# result = result.split(" ")
#
# for a in result:
#     new_result.append(a.capitalize())
# result = "".join(new_result)
#
# result = f"{hashtag}{result}"
#
# if len(result) > 140:
#     result = result[:140]
#
# print(result)



# my_list = [1, 8, 2, 3, 4, 5]

# my_list = [
#     100,    #тут лежить щось
#     2500,   #attitude
#     372,
#     498,
#     5762,
#     5,
#     66,
# ]

# my_list = []
# print(my_list)
#
# for value in range(5):
#     my_list.append(value)
#
# print(my_list)

# my_list = [value**2 for value in range(5)]
#
# print(my_list)

# my_list = [value ** 2 for value in range(5) if value // 2]
#
# print(my_list)

############## Tuple ###############

# value_tuple = tuple()
# value_tuple = (1,)
# print(value_tuple, type(value_tuple))


# value_tuple = (1, 2, 3, 4)
#
# value_list = list(value_tuple).append(5)
#
# value_tuple = tuple(value_list)

# value_tuple = (1, 2, 3, "hello", [12, 3])
# # value_tuple = (id, id, id, id, link)
#
# print(id(value_tuple))
# value_tuple[-1].append("а ось і можна")
#
# print(value_tuple, id(value_tuple))
# # value_tuple = (id, id, id, id, link)

# coordinates = (55.76343, 784.8888, 882.999)
#
# # latitude, longitude, attitude, *tmp = coordinates
#
# latitude, longitude, _, *tmp = coordinates


############# Dict ###########

# value_dict = {
#     1: "Nick",
#     2: "Denys",
#     "name": "Sasha",
#     True: "Nastia",
#     1.2: "Bella",
#     (1, 2, 3): "Vasia",
#     # [1, 2]: "Vova",
# }
#
#
# # print(value_dict)
#
# print(hash("Sasha"))
































