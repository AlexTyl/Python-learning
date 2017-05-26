"""Определить количество цифр, меньших 5, используемых при записи натурального числа N"""

number = 2630298349;
counter_of_numbers_less_then_five = 0;
while number != 0:
    current_num = number%10;
    number //= 10;
    if current_num < 5:
        counter_of_numbers_less_then_five += 1;
print(counter_of_numbers_less_then_five);