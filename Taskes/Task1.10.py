# Найти все меньшие N числа-палиндромы, которые при возведении в квадрат дают палиндром.
# Число называется палиндромом, если его запись читается одинаково с начала и с конца.

print("Enter the number: ")


def numerals_revers(number):
    revers_number = 0
    while number != 0:
        revers_number = revers_number * 10 + number % 10
        number //= 10
    return revers_number


def check_palindrome(number):
    return number == numerals_revers(number)


def palindrome_in_square_palindrome(number):
    return check_palindrome(number) and check_palindrome(number ** 2)


number = int(input())
i = 0

while i < number:
    if palindrome_in_square_palindrome(i):
        print(str(i))
    i += 1