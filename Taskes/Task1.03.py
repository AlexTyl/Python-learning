"""Выяснить, образуют ли цифры данного натурального числа N возрастающую оследовательность."""

print("Enter the number:")


def more_one_numeral(number):
    if (number // 10):
        return number
    else:
        print("Enter correct number:")
        number = more_one_numeral(int(input()))
    return number


def ascending_sequence_numerals(number):
    while number != 0:
        first_num = number % 10
        second_num = (number // 10) % 10
        if first_num < second_num:
            return False
        number //= 10
    return True


print(ascending_sequence_numerals(more_one_numeral(int(input()))))