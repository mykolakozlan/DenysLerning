
#
# my_dict = {}
# my_dict = dict(
#     name="John",
#     age=24
# )


# my_dict = {
#     "name": "John",
#     "age": 24,
#     "country": "UA",
#     "grade": 5
# }
#
# print(my_dict)
# print(my_dict["grade"])

# update()

# my_dict["type"] = "human"
# my_dict["type_1"] = "human"
# my_dict["type_2"] = "human"
# my_dict["type_3"] = "human"
# my_dict["type_4"] = "human"

# what_we_want_to_add = {
#     "type": "human",
#     "type_1": 24,
#     "type_2": "UA",
#     "type_3": 5,
#     "type_4": 5
# }
#
# my_dict.update(what_we_want_to_add)
#
#
# print(my_dict)
# # my_dict["age"] = 30
# # my_dict["type"] = "human"
#
# print(my_dict)


# user_info = {
#     "name": "John",
#     "email": "test@yesy.com",
#     "age": 24,
#     "country": "UA",
#     "grade": 5
# }
# json
# get()

# email = user_info.get("email", False)
# if not email:
#     print("ERROR: email is a mandatory field")

# print(my_dict["name"])

# pop()
# print(user_info)
# deleted_value = user_info.pop("name")
#
# print(deleted_value)
# print(user_info)

# user_info = {
#     "name": "John",
#     "email": "test@yesy.com",
#     "age": 24,
#     "country": "UA",
#     "grade": 5
# }

# for i in user_info:
#     print(i)

# keys()
# print(user_info.keys())
# for key in user_info.keys():
#     print(key)

# values()
# print(user_info.values())
#
# for value in user_info.values():
#     print(value)

# items()
# for key, value in user_info.items():
#     print(key, value)


# my_dict = dict.fromkeys(["name", "email"], "")
#
# print(my_dict)
# my_dict["name"] = "John"
#
# print(my_dict)

# my_dict = dict.fromkeys(["name_list", "email_list"], [])
#
# print(my_dict)
# my_dict["name_list"].append("John")
#
# print(my_dict)

# OrderDict, DefaultDict

from collections import OrderedDict, defaultdict, namedtuple

# user_info = {
#     "name": "John",
#     "email": "test@yesy.com",
#     "age": 24,
#     "country": "UA",
#     "grade": 5
# }

# user_info_ordered = OrderedDict(user_info)
#
# print(user_info)
# print(user_info_ordered) #OrderedDict[('name', 'John'), ('email', 'test@yesy.com'), ('age', 24),]

# defaultdict

# default_dict_val = defaultdict(list)
#
# print(default_dict_val)
#
# for i in range(5):
#     default_dict_val[i].append(i * 5)
#
# # print(default_dict_val)




############################ Dict Comprehension ##############


# some_dict = {}
#
# # some_list = [i * 2 for i in range(5)]
# some_dict = {key: f"Our value for {key}" for key in range(5)}
#
# # for key in range(5):
# #     some_dict[key] = f"Our value for {key}"

# print(some_dict)


############################## Set ################################

# my_list = [1, 2, 3, 4, 5, 6, 8, 3, 1]
# my_list = ["Name", "hello", "red"]

# print(my_list)
# print(set(my_list))


# print(hash(894392892034321942890333324))
# print(hash(1475006327104822538))


# my_set_1 = {1, 2, 3, 4}
# # my_set_2 = {"red", "green", "black", "white", 2, 3}
# #
# # # print(my_set_1.union(my_set_2)) #обʼєднання двох сетів
# # # print(my_set_1.difference(my_set_2)) # значення які не представлені в другому сеті
# # # print(my_set_1.intersection(my_set_2)) #на перерізі(те що представлено у обох сетах)
# # print(my_set_1)
# #
# # my_set_1.add(7)
# # my_set_1.add(40)
# # my_set_1.add(20)
# # print(my_set_1)
#
# frozen_set = frozenset(my_set_1)
# print(frozen_set)



# namedtuple

value_tuple = (1, 2, 3)

car_1 = ("Camry", 2.5, "black")
car_2 = ("Golf", 2.0, "green")

# car_model, engine, color


fields = ("model", "engine", "color")

car = namedtuple("Car", fields)
my_car = car("Golf", 2.0, "green")

print(my_car)
print(my_car.model)
print(my_car.color)
print(my_car.engine)







