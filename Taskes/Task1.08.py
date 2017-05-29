# Получить все четырехзначные целые числа, в записи которых нет одинаковых цифр

def identical_digits(number):
    while number != 0:
        current_number = number % 10
        check_number = number // 10
        while check_number != 0:
            if current_number == check_number % 10:
                return True
            check_number //= 10
        number //= 10
    return False


number = 1000

while number != 10000:
    if not identical_digits(number):
        print(str(number))
    number += 1