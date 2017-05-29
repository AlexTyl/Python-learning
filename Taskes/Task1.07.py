# Выяснить, есть ли в записи натурального числа N две одинаковые цифры

print("Enter number:")


def more_one_numeral(number):
    if (number // 10):
        return number
    else:
        print("Enter correct number:")
        number = more_one_numeral(int(input()))
    return number


def two_identical_digits(number):
    while number != 0:
        current_number = number % 10
        check_number = number // 10
        while check_number != 0:
            if current_number == check_number % 10:
                return True
            check_number //= 10
        number //= 10
    return False


print(two_identical_digits(more_one_numeral(int(input()))))