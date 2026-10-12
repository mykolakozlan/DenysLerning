


# option 1

#
# def popular_words(my_tekst, my_list):
#     new_list = my_tekst.lower().split(" ")
#
#     my_result = {word: new_list.count(word) for word in my_list}
#
#     # my_result = {}
#     # for x in my_list:
#     #     my_result.update({x: new_list.count(x)})
#
#     return my_result
#     # return {word: my_tekst.lower().split(" ").count(word) for word in my_list}
#
# print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')


# option 2


# def list_lowercase_only(my_str):
#     return [x for x in my_str.lower().split(" ")]
#
#
# def count_values_to_dict(new_list, my_list):
#     # result = {}
#     # for x in my_list:
#     #     summ_count = new_list.count(x)
#     #     result.update({x: summ_count})
#     #
#     return {word: new_list.count(word) for word in my_list}
#
#
# def popular_words(my_str, my_list):
#
#     return count_values_to_dict(list_lowercase_only(my_str), my_list)
#
#
# print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')


# option 3

# def popular_words(my_tekst, my_list):
#     new_list = my_tekst.split(" ")
#     new_list_1 = list(map(lambda x: x.lower(), new_list))
#
#     my_result = {}
#     for x in my_list:
#         result = new_list_1.count(x)
#         my_result.update({x: result})
#     return my_result
#
# print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')

# new_list_1 = map(lambda x: x.lower(), ['I', 'was', 'Three', 'near'])
# new_list_1 = list(map(lambda x: x.lower(), ['I', 'was', 'Three', 'near']))
# print(new_list_1)





# option 1

#
# def difference(*args):
#     if args == ():
#         return 0
#
#     min_value = args[0]
#     max_value = args[0]
#     for x in args:
#         if x < min_value:
#             min_value = x
#         if x > max_value:
#             max_value = x
#
#     result = max_value - min_value
#
#     return round(result, 1)
#
#
# print(difference(14.2, 2, -1))
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')


# option 2
# def my_min_value(*args):
#     min_value = args[0]
#     for x in args:
#         if x < min_value:
#             min_value = x
#     return min_value
#
#
# def my_max_value(*args):
#     max_value = args[0]
#     for x in args:
#         if x > max_value:
#             max_value = x
#     return max_value
#
#
# def first_difference_values(max_value, min_value):
#     return max_value - min_value
#
#
# def difference(*args):
#     if args == ():
#         return 0
#
#     min_value = my_min_value(*args)
#     max_value = my_max_value(*args)
#
#     result = first_difference_values(max_value,min_value)
#
#     return round(result, 1)
#
#
# print(difference(14.2, 2, -1))
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')


# option 3


# def difference(*args):
#
#     if args == ():
#         return 0
#
#     result = max(args) - min(args)
#     return round(result, 1)
#
#     # return round(max(args) - min(args), 1)
#
#
# difference(14.2, 2, -1)
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')









# Замикання (closures)

# def add(q, w):
#     return q + w
#
# a = add # Створення синоніму функції
# print(a(2, 3))





# # """Область видимості параметра n належить до зовнішньої (охоплюючій) функції, проте
# # вкладена функція може використовувати його. (LEGB)"""
# #
# def calculate_pow(n): # охоплююча функція
#
#     def calculate(number): # Вкладена функція
#         print(locals())
#
#         return number ** n # змінна з охоплюючої функції
#
#     return calculate # Возврат вложенной функции
#
# f = calculate_pow(3) # Виклик охоплюючої функції
# f_2 = calculate_pow(2) # Виклик охоплюючої функції
#
# print(f) # покажчик на вкладену функцію
# number_one = f(2) # Виклик вкладеної функції
# number_two = f_2(5)
# print(number_one)
# print(number_two)









# LEGB

# Використання модифікатора nonlocal

#
# def fibonacci():
#     first_number = 0
#     second_number = 1
#     def get_next():
#
#         nonlocal second_number #оголошуємо змінну не локальною
#         nonlocal first_number
#
#         next_number = second_number + first_number
#         first_number = second_number
#         second_number = next_number
#         return next_number
#     return get_next































# Decorators

# my_function = []
# #
# #
# def add_function(func):
#     """
#     Функція приймає на вхід будь-який об'єкт (функцію), додає його до
#     списку my_function і повертає цей об'єкт.
#      """
#     my_function.append(func)
#     return func


# @add_function # Застосування створеної функції як декоратор
# def summ(x, y): # Декорована функція
#     return x + y
#
#
# # summ = add_function(summ)
#
#
# @add_function
# def mul(x, y): # Декорована функція
#     return x * y
#
#
# print(my_function) # Список функцій, які ми задекорували
# print(summ(4, 5)) # функція працює так, як і було задумано






#
# # Створимо ще одну функцію і застосуємо до неї декоратор
# def div(q, w):
#     return q / w
#
# div = add_function(div)
#
# # @add_function
# # def div(q, w):
# #     return q / w
#
# print(my_function)
#
# print(div(5, 6))






# Передача параметрів для функції, що декорується.


# def to_str(func):
#     #конструкція *args, **kwargs дозволяє приймати будь-які аргументи (позиційні та/або іменовані) та в будь-якій кількості
#     def get_str(*args, **kwargs): # Функція, яка приймає аргументи для функції, що декорується
#         """from any type to string"""
#         return str(func(*args, **kwargs))
#
#     return get_str # Як результат повертається інша функція
#
#
# @to_str
# def suma(x, y):
#     return x + y
#
#
# # print("Summa = " + suma(3, 4)) #хоча функція suma повертає число, але тут помилка не виникне
# print(suma(3, 4), type(suma(3, 4))) #хоча функція suma повертає число, але тут помилка не виникне

# suma = to_str(suma)
# suma = get_str(*args, **kwargs) -> str(func(*args, **kwargs))

# print(suma) # бачимо вказівник на функцію get_str





# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     return inner
#
#
# @trace # identity = trace(identity)
# def identity(x):
#     """I do nothing useful."""
#     return x
#
#
# # print(identity(50))
# #
# print(identity) # вказівник на функцію inner
# help(identity) # Help on function inner
#
# print(identity.__name__, identity.__doc__) ##інформація з оригінальної функції









# # встановимо "правильні" значення в атрибути функції, що декорується:
# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     # Встановлюємо для функції inner значення, які були у декорованої функції
#     inner.__module__ = func.__module__
#     inner.__name__ = func.__name__
#     inner.__doc__ = func.__doc__
#     return inner
#
# @trace
# def identity(x):
#     """I do nothing useful."""
#     return x
#
# print(identity.__name__, identity.__doc__) ##інформація з оригінальної функції



















import functools

# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     functools.update_wrapper(inner, func)
#     return inner
#
# @trace
# def identity(x):
#     """I do nothing useful."""
#     return x
#
# print(identity.__name__, identity.__doc__)










# same with @wraps

def trace(func):
    """Декоратор trace виводить на екран повідомлення з
         інформацією про виклик функції, що декорується"""

    @functools.wraps(func)
    def inner(*args, **kwargs):
        """Inner doc"""
        print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return inner


@trace
def identity(x):
    """I do nothing useful."""
    return x


print(identity.__name__, identity.__doc__)
print(identity(34))

