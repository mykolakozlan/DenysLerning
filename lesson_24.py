

# class Cat:
#     arms_num = 4
#
#     def __init__(self, name, age, color, sound):  # метод додавання атрибутів у екземпляр класу
#         self.name = name
#         self.age = age
#         self.color = color
#         self.sound = sound
#
#     def __str__(self):
#         return f"This is a cat, it's name {self.name}, it's age {self.age}"
#
#     def __repr__(self):
#         return f"This is {self.name}"
#
#     @staticmethod
#     def cat_sound(sound):
#         return "Cat said " + sound
#
#     def cat_sound(self):
#         return "Cat said " + self.sound
#
#
#
# cat_1 = Cat("Barsik", 5, "black", "Hello")
# cat_2 = Cat("Tom", 3, "white", "Meow")
# cat_list = [cat_1, cat_2]
#
# print(cat_1.cat_sound(cat_1.sound))
#
# # print(cat_sound())
# # print(cat_list)
# # print(Cat.cat_sound())
# #
# # print(Cat.name)
# # print(Cat.age)







#
# class Phone(object):
#
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
#
#
#
#
# # #  Додамо на склад кілька ноутбуків
# notebook = Laptop('HP', 'ProBook 450', 35000)
# notebook1 = Laptop('HP', 'Laptop 15s-eq2054ur', 42000)
# wh.add_to_storage(notebook, 10)
# wh.add_to_storage(notebook1, 3)
# # print(wh.get_total_value())
# print(wh)






# from datetime import date
#
#
# class Person(object):
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
#     # Метод, який не пов'язаний зі змінними ні цього класу, ні його екземплярів
#
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
#
# print(person2.age)
# print(person3.age)













# class Animal(object):
#
#     def __init__(self, food, color):
#             self.food = food
#             self.color = color
#
#     def animal_sound(self):
#         return "Animal says: "
#
#     # def __str__(self):
#     #     return "Animal test"
#
#
# class Tiger(Animal):
#
#     def __init__(self, food, color, name, age):
#             self.name = name
#             self.age = age
#             super().__init__(food, color)
#
#     def animal_sound(self):
#         return super().animal_sound() + "Rrhhh"

    # def __str__(self):
    #     return "Tiger test"

# tiger_1 = Tiger("meat", "orange", "Sebastian", 3)
#
# print(tiger_1)
# print(tiger_1.animal_sound())
# print(tiger_1.food)



# class Animal:
#     """Клас, в якому знаходяться поля, характерні для великої підгрупи.
#        У всіх тварин є вік, раціон харчування та забарвлення
#     """
#
#     def __init__(self, age, ration, color):
#         self.age = age
#         self.ration = ration
#         self.color = color
#
#     def get_voice(self):
#         """Базовий метод, не прив'язаний до конкретного типу тварин  """
#         return 'Animal'
#
#     def __str__(self):
#         return f"age = {self.age}, ration = {self.ration}, color = {self.color}"
#
#
# class Cat(Animal):  # клас Cat є спадкоємцем Animal
#
#     def __init__(self, age, ration, color, name, cat_type):
#         # Для того, щоб був ініційований екземпляр Animal, необхідно в явному вигляді викликати метод __init__ цього класу
#         super().__init__(age, ration, color)  # функція super "знає", хто є батьком цього класу
#         self.name = name
#         self.cat_type = cat_type
#
#     def get_voice(self):
#         # за допомогою функції super, отримаємо результат роботи методу з батьківського класу
#         res = super().get_voice()
#         return res + " Meow"
#
#     def __str__(self):
#         return f"Cat: {super().__str__()} , name = {self.name}, cat_type = {self.cat_type}"


# class Dog(Animal):
#
#     def __init__(self, age, ration, color, name, dog_type):
#         super().__init__(age, ration, color)
#         self.name = name
#         self.dog_type = dog_type
#
#     def get_voice(self):
#         return "Woof"
#
# barsik = Cat(3, 'meat', 'black', 'Barsik', 'pers')
# # print(barsik)
# print(barsik.get_voice())
#
# dog = Dog(3, 'meat', 'black', 'Рes', 'BullDog')
# print(dog.get_voice())



#
#


















# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):  # Вказуємо клас ABC як батьківський
#
#     def __init__(self, age, ration, color):
#         self.age = age
#         self.ration = ration
#         self.color = color
#
#     @abstractmethod  # Створюємо метод, який обертаємо за допомогою декоратора
#     def get_voice(self):  # raise TypeError
#         pass
#
#
# class Fox(Animal):
#
#     def __init__(self, age, ration, color, name, fox_type):
#         super().__init__(age, ration, color)
#         self.name = name
#         self.fox_type = fox_type
#
#     def get_voice(self):
#         return "Fox"
#
#
# fox = Fox(3, 'meat', 'black', 'fox', 'red_fox')
# print(fox.get_voice())




# class Base:
#
#     def price(self):
#         return 10
#
#
# class InterFoo(Base):
#
#     def price(self):
#         return Base.price(self) * 1.1
#
#
# class Discount(InterFoo):  # <--
#
#     def price(self):
#         return InterFoo.price(self) * 0.8



# class Base:
#
#     def price(self):
#         return 10
#
# class InterFoo(Base):
#     def price(self):
#         return super().price() * 1.1 # Тут через super().price() ми звертаємося до методу price у класі Base
#
# class Discount(InterFoo):
#
#     def price(self):
#         return super().price() * 0.8 # Тут через super().price() ми звертаємося до методу price у класі InterFoo
#
#


# class A:  # (object)
#     def print_smile(self):
#         print(":)")
#
#
# class B(A):
#     def print_sad_smile(self):
#         print(":(")
#
# class C(B):
#     def print_both_smile(self):
#         print(":( :)")
#
# class D(C):
#     # def print_sad_smile(self):
#     #     print("^)")
#     pass
#
#
# example = D()
# example.print_sad_smile()
# example.print_smile()
# example.print_both_smile()
#



######################################## ччв    ч1 (Method Resolution Order) ############################################


# # MRO – (Method Resolution Order)
# print(D.mro())
# print(D.__mro__)


# class D:
#
#     def print_smile(self):
#         print (":P)")
#
#
# class A(D):
#     pass
#
#
# class B:
#
#     def print_smile(self):
#         print(":(")
#
#     def __str__(self):
#         return "B str"
#
#
# class C(A, B):
#     pass
#
# my_var = C()
# # my_var.print_smile() # Пошук атрибутів у класах батьках, завжди йде зліва направо, і знизу вгору
# print(my_var)
# print(C.mro())



