"""Найти все четные четырехзначные числа, цифры которых следуют в порядке возрастания или убывания."""


def ascending_sequence_numerals(number):
    while number != 0:
        first_num = number % 10
        second_num = (number // 10) % 10
        if first_num < second_num:
            return False
        number //= 10
    return True


def decreasing_sequence_numerals(number):
    while number != 0:
        if number // 10 == 0:
            return True
        first_num = number % 10
        second_num = (number // 10) % 10
        if first_num > second_num:
            return False
        number //= 10
    return True

number = 1000

while number != 10000:
    if ascending_sequence_numerals(number):
        print("ascending: "+str(number))
    elif decreasing_sequence_numerals(number):
        print("decreasing: "+str(number))
    number += 2
