# Получить  все  четырехзначные  числа,  в  записи  которых  встречаются только цифры 0,2,3,7.


def check_valid_number(number):
    while number != 0:
        if number % 10 in [1, 4, 5, 6, 8, 9]:
            return False
        number //= 10
    return True

number = 1000

while number != 10000:
    if check_valid_number(number):
        print(str(number))
    number += 1