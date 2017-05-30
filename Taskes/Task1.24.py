# Напечатать  натуральное  число  N :
# а) в  двоичной  системе  счисления;
# б) в шестнадцатеричной системе счисления.


print("Enter the number: ")


def decimal_to_binary(number):
    if number == 0:
        return str(number)
    binary_number = ""
    while number != 0:
        if number % 2 == 1:
            binary_number = '1' + binary_number
        else:
            binary_number = '0' + binary_number
        number //= 2
    return binary_number


def decimal_to_hexadecimal(number):
    if number == 0:
        return "0x" + str(number)
    hexadecimal_number = ""
    hexadecimal_alphabet = "0123456789ABCDEF"
    while number != 0:
        hexadecimal_number = hexadecimal_alphabet[number % 16] + hexadecimal_number
        number //= 16
    return "0x" + hexadecimal_number


n = int(input())

print("binary: "+decimal_to_binary(n))

print("hexadecimal: "+decimal_to_hexadecimal(n))