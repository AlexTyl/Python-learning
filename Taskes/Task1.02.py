"""Получить все четырехзначные числа, сумма цифр которых равна заданному числу n."""


def summ_of_numerals(number):
    sum_numeral = 0
    while number != 0:
        sum_numeral += number % 10
        number //= 10
    return sum_numeral


def summ_of_numerals_equals_number(number):
    counter_num = 1000
    while counter_num < 10000:
        if number == summ_of_numerals(counter_num):
            print(counter_num)
        counter_num += 1


def summ_of_numerals_equals_number_v2(my_list, number):
    for i in my_list:
        if summ_of_numerals(i) == number:
            print(i)

print("Enter the number:")
summ_of_numerals_equals_number(int(input()))


print("Enter start and end of array:")
start = int(input())
end = int(input())

print("Enter the number:")

summ_of_numerals_equals_number_v2(range(start, end), int(input()))
