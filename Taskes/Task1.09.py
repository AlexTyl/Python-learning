# Дано  натуральное  число  N.  Определить,  является  ли  оно  автоморфным.
# Автоморфное число  равно последним разрядам квадрата этого числа. Например,  5 и 25,  6 и 36,  25 и 625.

print("Enter the number: ")


def check_automorphic(number):
    square_number = number ** 2
    while number != 0:
        if number % 10 != square_number % 10:
            return False
        number //= 10
        square_number //= 10
    return True


print(check_automorphic(int(input())))