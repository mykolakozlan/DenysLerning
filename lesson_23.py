

###################### OOP ######################

# Наслідування, Інкапсуляція, Поліморфізм              Абстракція, Композиція


# class Car:
#     color = "white"     # атрибут
#
#
# car_1 = Car()           # екземпляр
# car_1.stick = "Heyyy"   # атрибут екземпляру
#
#
# car_2 = Car()



# class Car(object):
#
#     def __init__(self, color, engine, price):
#         self.color = color
#         self.engine = engine
#         self.price = price
#
#
#
#
# car_1 = Car("white", "1.8", "5000")           # екземпляр
# print(car_1.color)   # атрибут екземпляру
# print(car_1.engine)   # атрибут екземпляру
#
#
# car_2 = Car("red", "2.5", "15000")
# print(car_2.color)   # атрибут екземпляру
# print(car_2.engine)


# class Cat:
#
#     def __new__(cls, *args, **kwargs): # метод, який насправді створює екземпляр класу
#         print("Creating Cat instance")
#         self = super().__new__(cls) # про функцію super() трохи пізніше
#         print(self)
#         return self # instance
#
#     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
#         print("Cat instance fields")
#         self.name = name
#         self.age = age
#         self.color = color
#
# cat = Cat("Barsik", 5, "black")
# print(cat)

#
# def cat_sound():
#     return "Meow"


# class Cat:
#
#
#     def __init__(self, name, age, color):  # метод додавання атрибутів у екземпляр класу
#         self.name = name
#         self.age = age
#         self.color = color
#
#
#     def __str__(self):
#         return f"This is a cat, it's name {self.name}, it's age {self.age}"
#
#
#     def __repr__(self):
#         return f"This is {self.name}"
#
#
#     @staticmethod
#     def cat_sound():
#         return "Meow"
#
#
#
# cat_1 = Cat("Barsik", 5, "black")
# cat_2 = Cat("Tom", 3, "white")
# cat_list = [cat_1, cat_2]
#
# print(cat_sound())
# # print(cat_list)
# # print(Cat.cat_sound())















# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f'Phone {self.brand} {self.model} {self.price}'
#
#
# class Laptop:
#     def __init__(self, brand, model, price):
#         # Важливо, щоб набір полів був схожим на інші класи, які зберігаються на складі
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f'Laptop {self.brand} {self.model} {self.price}'

#
#
#
#
#
# # Створимо кілька екземплярів класу Phone
# phone1 = Phone('Samsung', 'A52', 7000)
# # print(phone1)
# phone2 = Phone('Samsung', 'S11', 37000)
# phone3 = Phone('Samsung', 'A12', 4000)
# phone4 = Phone('Xiaomi', 'Redmi Note 11 ', 8700)
# phone5 = Phone('Xiaomi', '12 Lite', 17000)
# # print(phone5)
# #
# # # print(hash(phone1))
# #
# #
# class Warehouse:
#
#     def __init__(self, address):
#         self.address = address
#         self.storage = {}
#
#     def add_to_storage(self, item, value):
#         """ Метод додавання товару на склад """
#         self.storage[item] = value
#
#     def remove_from_storage(self, item):
#         """ Метод видалення товару зі складу """
#         value = self.storage.pop(item, None)
#         return value
#
#     def get_item_value(self, item):
#         """ Метод отримання кількості товару на складі """
#         return self.storage.get(item)
#
#     def get_total_value(self):
#         """ Метод отримання загальної вартості товару на складі """
#         total = 0
#         for key, cnt in self.storage.items():
#             total += key.price * cnt
#         return total
#
#     def __str__(self):
#         """ Метод виведення інформації про склад """
#         tmp = ''
#         for item, cnt in self.storage.items():
#             tmp += f'{str(item)}: {cnt} pcs. \n'
#         return f'Warehouse at {self.address} contains:\n{tmp} '
#
#
# wh = Warehouse('Kyiv, vul. Viskozna, 135')
# # print(wh.get_total_value())  # На складі нічого немає
# # #  Додамо на склад кілька телефонів і перевіримо деякі методи
# wh.add_to_storage(phone1, 40)
# wh.add_to_storage(phone2, 23)
# # print(wh.get_total_value())
#
# wh.add_to_storage(phone3, 4)
# wh.add_to_storage(phone4, 52)
# wh.add_to_storage(phone5, 22)
# # print(wh.get_total_value())
#
#
# # # # # # Видалимо кілька телефонів і перевіримо інформацію по складу
# # # print(wh.remove_from_storage(phone2))
# # # print(wh.get_item_value(phone2))
# # # print(wh)
# #
# #
# #
# #
# #
# # #  Додамо на склад кілька ноутбуків
# notebook = Laptop('HP', 'ProBook 450', 35000)
# notebook1 = Laptop('HP', 'Laptop 15s-eq2054ur', 42000)
# wh.add_to_storage(notebook, 10)
# wh.add_to_storage(notebook1, 3)
# # print(wh.get_total_value())
# print(wh)






# from datetime import date
#
# class Person:
#
#     # Дозволяє обчислити дані, і повернути новий екземпляр класу, з цими даними
#     @classmethod
#     def from_birth_year(cls, name, year):
#         return Person(name, date.today().year - year)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # Метод, який не пов'язаний зі змінними ні цього класу, ні його екземплярів
#     @staticmethod
#     def is_adult(age):
#         return age > 18
#     # # Метод, який не пов'язаний зі змінними ні цього класу, ні його екземплярів
#     #
#     # def is_adult(self):
#     #     return self.age > 18
#
#
# person1 = Person('Michael', 16)
# person2 = Person.from_birth_year('John', 1996)
# person3 = person2.from_birth_year('mayank3', 2000)
# #
# print(person1.age)
# print(person1.is_adult(person1.age))

print(person2.age)
print(person3.age)
