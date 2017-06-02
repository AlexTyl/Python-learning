# Получить  все  четырехзначные  числа,  в  записи  которых  встречаются только цифры 0,2,3,7.


def check_valid_number(number):
    number = abs(number)
    while number != 0:
        if number % 10 in [1, 4, 5, 6, 8, 9]:
            return False
        number //= 10
    return True

#2037
def check_valid_number_V2(number):
    number = abs(number)
    while number != 0:
        flag = False;
        defualtNumber = 2037;
        while defualtNumber != 0:
            if(number % 10 == defualtNumber % 10):
                flag = True;
            defualtNumber //= 10;
        if(not flag):
            return False
        number //= 10
    return True

number = 1000

while number != 10000:
    if check_valid_number_V2(number):
        print(str(number))
    number += 1