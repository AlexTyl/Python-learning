# Натуральное число N разложить на простые множители

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


def simple_multipliers(number):
    if check_prime_number(number):
        return str(number) + " is simple"
    multipliers = "1"
    current_multiplier = 2
    while number != 1:
        if check_prime_number(current_multiplier) and number % current_multiplier == 0:
            multipliers = multipliers + " * " + str(current_multiplier)
            number //= current_multiplier
            current_multiplier = 1
        current_multiplier += 1
    return multipliers


print(simple_multipliers(int(input())))