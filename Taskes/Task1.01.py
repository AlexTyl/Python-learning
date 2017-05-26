"""Определить количество цифр, меньших 5, используемых при записи натурального числа N"""

number = 2630298349;
counter_of_numbers_less_then_five = 0;
while number != 0:
    if  number%10 < 5:
        counter_of_numbers_less_then_five += 1;
    number //= 10;
print(counter_of_numbers_less_then_five);