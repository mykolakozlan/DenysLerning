# first_symbol = float(input("1st num:  "))
# my_operator = input("operator (+, -, /, *):  ")
# second_symbol = float(input("2nd num:  "))
#
# result = None
#
# # len()
#
# # if my_operator != "+" or my_operator != "-" or my_operator != "*" or my_operator != "/":
# # if my_operator not in "+-*/" or len(my_operator) != 1:
# # if my_operator not in ["+", "-", "*", "/"]:
# if my_operator not in ("+", "-", "*", "/"):
#     result = "ERROR: Wrong operator"
# else:
#     if my_operator == "+":
#         result = first_symbol + second_symbol
#     elif my_operator == "-":
#         result = first_symbol - second_symbol
#     elif my_operator == "*":
#         result = first_symbol * second_symbol
#     elif my_operator == "/":
#         if second_symbol != 0:
#             result = first_symbol / second_symbol
#         elif second_symbol == 0:
#             result = "ERROR: Can't divide by zero"
# # else:
# #     print("ERROR: Wrong operator")
#
#
# print(result)










# original_list =  [12, 3, 4, 5]

# if len(original_list) == 0:
#     print(original_list)
# else:
#     # last_element = original_list[-1]
#     # test = original_list.pop()



# original_list =  [2, 5]
#
# if len(original_list) > 1:
#     original_list.insert(0, original_list.pop())
#
# print(original_list)









# my_list = [1, 2, 3, 9, 4, 5, 6]

# separator = len(my_list) - len(my_list) // 2
# new_list = [my_list[:separator], my_list[separator:]]
#
# print(new_list)





# separator = 0
#
# if len(my_list) % 2 == 0:
#     separator = len(my_list) // 2
# else:
#     separator = (len(my_list) // 2) + 1
#
# new_list = [my_list[:separator], my_list[separator:]]
#
# print(new_list)


# separator = len(my_list) // 2
#
# if len(my_list) % 2 != 0:
#     separator += 1
#
# new_list = [my_list[:separator], my_list[separator:]]
#
# print(new_list)













################################### Loop #################################################

# while for
# else, break, continue, range, pass



# my_num = 0
# is_validate = True


# count = 4
#
# while True:
#     my_num += 1
#     if my_num == 5:
#         continue
#     print(my_num)
#     if my_num > 9:
#         break
# else:
#     print("end")
#
# print("Wait for 2 hours")

# while my_num < 10:
#     my_num += 1
#     print(my_num)

# while is_validate:
#     my_num += 1
#     print(my_num)
#     if my_num > 10:
#         is_validate =  False
# else:
#     print("end")

# for

# value_str = "Hello"
# # value_str = 99
# value_str = True
# value_str = [1, 2, 34]
#
# my_index = 0

# while my_index < len(value_str):
#     print(value_str[my_index])
#     my_index += 1

# for letter in value_str:
#     print(letter)
#     # value_str.append(1)


# range()
# range(10) 0 до 10(не включно)
# range(2, 10) від 2 до 10(не включно)
# range(2, 10, 2) з кроком


# for number in range(3, 10, -1):
#     print(number)
    # continue
    # break
# else:
#     print("ffff")




# num = 10
#
# if num > 0:
#     # TODO Nikolas work
#     pass
# elif num < 0:
#     # TODO Denys work
#     """
#     It should work as .......
#     """
#     pass
# elif num == 0:
#     pass
# elif num != 0:
#     pass


# print("end")












# numbers_1 = int(input("Enter the first number: "))
# numebrs_2 = input("Enter the operation:")
# numebrs_3 = int(input("Enter the second number:"))
#
# match numebrs_2:
#     case "+":
#         print(int(numbers_1 + numebrs_3))
#     case "-":
#          print(int(numbers_1 - numebrs_3))
#     case "*":
#          print(int(numbers_1 * numebrs_3))
#     case "/":
#          if numebrs_3 != 0: print(int(numbers_1 / numebrs_3))
#          elif numebrs_3 == 0: print("Cannot divide by zero")
#     case _:
#         print("error wrong operator")







