"""По заданному натуральному числу N получить число M,
записанное цифрами исходного числа, взятыми в обратном порядке."""


print("Enter the number N")


def numerals_revers(number):
    revers_number = 0
    while number != 0:
        revers_number = revers_number * 10 + number % 10
        number //= 10
    return revers_number

print("Number M = " + str(numerals_revers(int(input()))))
