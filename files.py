# ^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!*@#$%^&+=]).*$
# ^[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}$
# t_e@s.com
# ^[+]{0,1}[380][0-9]{7}$
# "^[a-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+$"

# import re
# - домашній номер телефону (тільки цифри та довжина номера)
# home_phone_numbers = ["123456", "1234", "1234567", "+12345"]
#
# for number in home_phone_numbers:
#     if re.match(r"^\d{6}$", number):
#         print(f"Phone number {number} is correct")
#     else:
#         print(f"Phone number {number} is not correct")

# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# mobile_phone_numbers = ["+380123456789", "380123456789", "+3801234567892", "+3801234567", "++380123456789"]
#
# for number in mobile_phone_numbers:
#     if re.match(r"^\+?\d{12}$", number):
#         print(f"Phone number {number} is correct")
#     else:
#         print(f"Phone number {number} is not correct")

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# emails = ["test@gmail.com", "test1@gmail.com", "test_1@gmail.com", "test2@gmail", "test_@gmail", "test_gmail"]
#
# for email in emails:
#     if re.match(r"^[0-9a-zA-Z]+[._]?[0-9a-zA-Z]+@[a-zA-Z0-9]+[.][a-zA-Z]{2,}$", email):
#         print(f"Email {email} is correct")
#     else:
#         print(f"Email {email} is not correct")

# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
# users = ["Vasya Vasya Vasya", "vasya vasya vasya", "vasya1 vasya vasya", "vasya_vasya vasya", "vasya vasya vasya vasya"]
#
# for user in users:
#     if re.match(r"^[A-ZА-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}\s[A-ZА-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}\s[A-ZА-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}$", user):
#         print(f"User {user} is correct")
#     else:
#         print(f"User {user} is not correct")

# додатково:
#
# - Пароль (мінімально: одна велика літера, одна маленька літера,
# одна цифра, один символ, довжина пароля – від 8 до 16 символів)
# passwords = ["Admin123!", "admin123!", "Admin123", "Admin!", "admin"]
# for password in passwords:
#     if re.match(r"^.*(?=.{8,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!*@#$%^&+=]).*$", password):
#         print(f"Password {password} is correct")
#     else:
#         print(f"Password {password} is not correct")

#######################
###
# r (Read). Файл відкривається для читання. Якщо файл не знайдено, то генерується виняток FileNotFoundError
#
# w (Write). Файл відкривається для запису. Якщо файл відсутній, він створюється. Якщо такий файл вже є,
# то він створюється заново, і відповідно старі дані в ньому стираються.
#
# a (Append). Файл відкривається для запису. Якщо файл відсутній, він створюється.
# Якщо подібний файл вже є, дані записуються в його кінець.
#
# b (Binary). Використовується для роботи з бінарними файлами. Застосовується разом з іншими режимами – w або r.

# # v1
# try:
#     my_file = open("hello.txt", "w")
#     try:
#         my_file.write("hello world")
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()
# except Exception as e:
#     print(e)
#
# # v2
# with open("hello_1.txt", "w") as test_file:
#     test_file.write("text1")
#
#
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("text2\ntext3\n")

#
# with open("hello.txt", "r") as myfile:
#     # v1
#     # result = myfile.read()
#     # print(result)
#     # v2
#     # result = myfile.readline()
#     # print(result, end="")
#     # result = myfile.readline(3)
#     # print(result)
#     # v3
#     # result = myfile.readlines()
#     # print(result)
#     # v4
#     # for line in myfile:
#     #     print(line, end="")
#     # v5
#     line = myfile.readline()
#     while line:
#         print(line, end="")
#         line = myfile.readline()

# ###
# FILENAME = "notes.txt"
# NOTES_COUNT = 3
#
# notes = []
#
# for i in range(NOTES_COUNT):
#     notes.append(input(f"Enter note: {i + 1}: ").strip())
#
# with open(FILENAME, "a") as file:
#     for i in range(NOTES_COUNT):
#         file.write(f"{i + 1}. {notes[i]}\n")
#
# with open(FILENAME, "r") as file:
#     print(file.read())

####
# import pickle
# FILENAME = "notes.dat"
#
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)  # серіалізація - запись в бинарный файл
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)  # десеріалізація - чтение из бинарного файла
#     for user in users_from_file:
#         print(f"Name: {user[0]} Phone: {user[1]}")

#
# import shelve
#
# FILENAME = "notes"
#
# with shelve.open(FILENAME) as users:
#     users["John"] = "123456789"
#     users["Peter"] = "987654321"
#     users["Vasya"] = "1568654156"
#
# with shelve.open(FILENAME) as users:
#     users["Petya"] = "12312341234123"
#     print(users["Petya"])
#     print(users["John"])
#
#     for key in users:
#         print(f"{key} - {users[key]}")
#
#     print(users)
#     users.pop("John", "not found")
#
#     print("-" * 10)
#
#     for key in users:
#         print(f"{key} - {users[key]}")

##########
# import csv
#
# FILENAME = "users.csv"
#
# users = [
#     {"name": "John", "phone": "111"},
#     {"name": "Petya", "phone": "222"},
#     {"name": "Vasya", "phone": "333"},
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     columns = ["name", "phone"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#
#     # all users
#     writer.writerows(users)
#
#     # one user
#     user: dict = {"name": "Test", "phone": "555"}
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['name'], " - ", row['phone'])

###
##
import os

# v1
# os.mkdir("test_folder")

# v2
# os.rmdir("test_folder")
#
# file_name = "users.csv"
# if os.path.exists(file_name):
#     os.remove(file_name)
#     print("File removed!")
# else:
#     print("File not found!")

# доп: написати скрипт для видалення всіх файлів вказаної директорії
#
# # відносний шлях - щодо поточної директорії (папки, де знаходиться вихідник, який ви запустили)
# with open("f1/f2/test.txt", "w") as myfile:
#     myfile.write("hello world")
#
# with open("../../test1.txt", "w") as myfile:
#     myfile.write("hello world")
# абсолютний шлях - повний шлях починаючи з диска C://test_folder/...
#####################################################################
# import json
#
# # json string data
# employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'
#
# # check data type with type() method
# print(type(employee_string))
#
# # convert string to  object
# json_object = json.loads(employee_string)
#
# # check new data type
# print(type(json_object))
#
# # output
# # <class 'dict'>
#
# # access first_name in dictionary
# print(json_object["first_name"])
#
# ####################
# employees_string = '''
# {
#     "employees" : [
#        {
#            "first_name": "Michael",
#            "last_name": "Rodgers",
#            "department": "Marketing"
#
#         },
#        {
#            "first_name": "Michelle",
#            "last_name": "Williams",
#            "department": "Engineering"
#         }
#     ]
# }
# '''
#
# data = json.loads(employees_string)
#
# print(type(data))
# # output
# # <class 'dict'>
#
# # access first_name
# for employee in data["employees"]:
#     print(employee["first_name"])
#
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))
###############
# import json
# import os
#
# PATH_TO_TODO_LIST = "myTodoList.json"
#
#
# def create_todo_list_json_file(path_to_storage: str) -> None:
#     if not os.path.exists(path_to_storage):
#         with open(path_to_storage, "w", encoding="utf-8") as file:
#             todos_dict: dict = {"todos": []}
#             file.write(json.dumps(todos_dict))
#     else:
#         raise FileExistsError("File already exists!")
#
#
# def get_todo_items(path_to_storage: str) -> dict:
#     with open(path_to_storage, 'r', encoding="utf-8") as file:
#         return json.load(file)
#
#
# def add_todo_item(path_to_storage: str, todo_item: str) -> str:
#     current_todos = get_todo_items(path_to_storage)
#     current_todos["todos"].append(todo_item)
#     with open(path_to_storage, 'w', encoding="utf-8") as file:
#         json.dump(current_todos, file, indent=4)
#         return todo_item
#
#
# def remove_todo_item(path_to_storage: str, todo_item: str) -> str:
#     current_todos = get_todo_items(path_to_storage)
#     current_todos["todos"].remove(todo_item)
#     with open(path_to_storage, 'w', encoding="utf-8") as file:
#         json.dump(current_todos, file, indent=4)
#         return todo_item
#
#
# if __name__ == "__main__":
#     if os.path.exists(PATH_TO_TODO_LIST):
#         print(get_todo_items(PATH_TO_TODO_LIST))
#         # add_todo_item(PATH_TO_TODO_LIST, "second item")
#         remove_todo_item(PATH_TO_TODO_LIST, "first item")
#         print(get_todo_items(PATH_TO_TODO_LIST))
#     else:
#         create_todo_list_json_file(PATH_TO_TODO_LIST)

# дописать меню
# добавить функцию изменения по порядковому номеру (от 1 до ...)
# протестировать все функции

