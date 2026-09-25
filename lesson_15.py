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


# def get_weather(temperature, sky_type):
#     res = ""
#
#     if temperature == 15 and sky_type == "cloudy":
#         res = "it's fine, but take your umbrella"
#     elif temperature > 15:
#         res = "It's hot"
#     elif temperature == 15:
#         res = "it's fine"
#     else:
#         res = "it's cold"
#
#     return res


# print(get_weather(20, "cloudy"))
#
# temp = 15
# sky = "cloudy"
# #
# # result = get_weather(temp, sky)
# #
# # print(result)
#
#
def get_weather(temperature, sky_type):
    res = ""

    if temperature == 15 and sky_type == "cloudy":
        res = "it's fine, but take your umbrella"
    elif temperature > 15:
        res = "It's hot"
    elif temperature == 15:
        res = "it's fine"
    else:
        res = "it's cold"

    return res
#
#
# print(get_weather(temp, sky))

# Правило доступу до змінних LEGB Local Enclosure Global Built-in

# from math import pi
#
# pi = "Global"
#
# def outer():
#     pi = "Enclosure"
#
#     def inner():
#         pi = "Local"
#         # global pi
#
#         pi += "!!!!"
#
#         print(pi)
#
#     inner()
#
# outer()

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











