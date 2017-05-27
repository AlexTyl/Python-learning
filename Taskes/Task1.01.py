"""Определить количество цифр, меньших 5, используемых при записи натурального числа N"""

print("Enter the number:")


def less_then_five_numerals_count(number):
    counter_of_numerals_less_then_five = 0
    while number != 0:
        if number % 10 < 5:
            counter_of_numerals_less_then_five += 1
        number //= 10
    return counter_of_numerals_less_then_five

print(less_then_five_numerals_count(int(input())))


