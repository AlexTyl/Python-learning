# Выяснить, есть ли в записи натурального числа N две одинаковые цифры

print("Enter number:")


def more_one_numeral(number):
    if (number // 10):
        return number
    else:
        print("Enter correct number:")
        number = more_one_numeral(int(input()))
    return number


def only_two_identical_digits(number):
    buffer_number = number
    while number != 0:
        check_number = buffer_number
        identical_digits_counter = 0
        current_number = number % 10
        while check_number != 0:
            if current_number == check_number % 10:
                identical_digits_counter += 1
            check_number //= 10
        if identical_digits_counter == 2:
            return True
        number //= 10
    return False


print(only_two_identical_digits(more_one_numeral(int(input()))))