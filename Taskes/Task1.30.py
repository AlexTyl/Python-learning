# Найти среди натуральных чисел n, n+1,...,2n-1 числа-близнецы,
#  т. е. два таких простых числа, разность между которыми равна двум.

print("Enter the number: ")


def check_prime_number(number):
    if number < 2:
        return False
    current_number = number - 1
    while current_number != 1:
        if number % current_number == 0:
            return False
        current_number -= 1
    return True


def twin_numbers(n):
    if n == 3:
        print("(3, 5)")
    for i in range(n, 2 * n - 3):
        if check_prime_number(i) and check_prime_number(i+2):
            print("("+str(i)+", "+str(i+2)+")")


twin_numbers(int(input()))