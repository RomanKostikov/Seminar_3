# 3. Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу",
# ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1
"""Doc."""
import os
os.system('cls')

test_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(f"список: {test_list}")
test_item = input("Введите искомую строку: ")


def check_list(test_list, test_item):
    count = 0
    for i in range(len(test_list)):
        if test_list[i] == test_item:
            count += 1
            if count == 2:
                return i
    else:
        return -1

# групповое решение
# print(f"ответ: {check_list(test_list, test_item)}")

# def find_index_coin(new_list, text, num=2):
#     count = 0
#     for i in range(len(new_list)):
#         if text == my_list[i]:
#             count += 1
#         if count == num:
#             return i
#     return -1


# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# print(find_index_coin(my_list, 'qwe'))
