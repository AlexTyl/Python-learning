# Найти наибольший общий делитель (НОД) двух натуральных чисел N и M.

print("Enter the N and M: ")


def greatest_common_divisor(n, m):
    if n > m:
        current_number = m
    else:
        current_number = n
    while current_number != 0:
        if n % current_number == 0 and m % current_number == 0:
            return current_number
        current_number -= 1


print(greatest_common_divisor(int(input()),int(input())))