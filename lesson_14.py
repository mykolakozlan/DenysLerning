# Функції
# Глобальні та локальні змінні.
# Передача аргументів.
# Правило доступу до змінних LEGB
# Використання іменованих параметрів.
# аргументи за замовчуванням
# Використання змінної кількості аргументів
# Використання змінної кількості іменованих аргументів
# Тонкощі використання аргументів
# Розпакування кортежу в низку фактичних параметрів
# Розпакування словника в низку фактичних параметрів
# Особливості використання функцій


# YAGNI  you ain't gonna need it


# import string
#

# value = input(str(" Enter your value in this format: a-d :"))
#
# def my_ascii_letters(val):
#     all_value = string.ascii_letters
#     string_value = ""
#
#     start_symbol, last_symbol = val.split("-")
#
#     index_start_symbol = all_value.find(start_symbol)
#     index_last_symbol = all_value.find(last_symbol)
#
#     if index_start_symbol != -1 and index_last_symbol != -1:
#         string_value = all_value[index_start_symbol:index_last_symbol + 1]
#
#     if index_start_symbol > index_last_symbol or string_value not in all_value:
#         return "Not in alphabetical order"
#     elif not string_value:
#         return "Not valid symbols"
#     else:
#         return string_value


# import string
#
# input_str = input('Enter two letters hyphenated: ')  # z-a -> ["a", "c"]
#
# if "-" in input_str and "-" != input_str[0] and "-" != input_str[2]:
#     input_str = input_str.split('-')
#
# beginning = string.ascii_letters.find(input_str[0])
# ending = string.ascii_letters.find(input_str[-1])
#
# if beginning == -1 or ending == -1:
#     print("error")
# else:
#     print(string.ascii_letters[beginning:ending + 1])


# value = int(input("Enter your number  :"))
#
# days = 0
# one_day = 24 * 60 * 60
# one_hour = 60 * 60
# one_minute = 60
# seconds = 0
#
# if value >= 0 and value < 8640000:
#
#     days, hours = divmod(value, one_day)
#     hours, minutes = divmod(hours, one_hour)
#     minutes, seconds = divmod(minutes, one_minute)
#
#     full_hours = (str(hours)).zfill(2)
#     full_minutes = (str(minutes)).zfill(2)
#     full_seconds = (str(seconds)).zfill(2)
#
#     if days == 1:
#         result = f"{days} day, {full_hours}:{full_minutes}:{full_seconds}"
#     else:
#         result = f"{days} days, {full_hours}:{full_minutes}:{full_seconds}"
#
#     print(result)
#
# else:
#     print("ERROR")



# client_input = input() #89lkjlk89 -> [89, 89]

# result = []
# current_number = ""
#
# for char in client_input:
#     if char.isdigit():
#         current_number += char
#     else:
#         if current_number:
#             result.append(current_number)
#             current_number = ""
#
# if current_number:
#     result.append(current_number)
#
# print(result)



##########################  Function  #########################################




# def my_func(num_1, num_2):
#
#     balance = num_1 + num_2
#
#     return balance
#
# print(my_func(7, 2))



# def my_calc(number_1, number_2, symbol):
#     """This func
#         is doing something
#         important!"""
#
#     result = 0
#
#     if symbol == "+":
#         result = add(number_1, number_2)
#     elif symbol == "-":
#         result = sub(number_1, number_2)
#
#     return result
#
#
# def add(num_1, num_2):
#     res = num_1 + num_2
#
#     return res
#
# def sub(num_1, num_2):
#     res = num_1 - num_2
#
#     return res
#
#
# print(my_calc(1, 2, "-"))


def say_hi(name, age):
    result = f"Hey I'm {name}. I'm {age} years old"

    return result


assert say_hi("Alex", 32) == "Hey I'm Alex. I'm 32 years old", "Test1"
assert say_hi("Frank", 68) == "Hey I'm Frank. I'm 68 years old", "Test2"

print("OK")