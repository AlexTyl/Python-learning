# В массиве А(N) первый положительный элемент и последний отрицательный элемент переставить местами.


def random_array(dimension, min_element, max_element):
    import random
    mass = []
    while dimension > 0:
        mass.append(random.randint(min_element, max_element))
        dimension -= 1
    return mass


def swap_last_negative_and_first_positive(mass):

    def index_of_last_negative_number(mass):
        current_index = len(mass) - 1
        while current_index > 0:
            if mass[current_index] < 0:
                return current_index
            current_index -= 1
        return -1

    def index_of_first_positive_number(mass):
        current_index = 0
        while current_index < len(mass):
            if mass[current_index] > 0:
                return current_index
            current_index += 1
        return -1

    index_last_negative = index_of_last_negative_number(mass)
    index_first_positive = index_of_first_positive_number(mass)

    if index_last_negative == -1 or index_first_positive == -1:
        return mass

    buffer = mass[index_first_positive]
    mass[index_first_positive] = mass[index_last_negative]
    mass[index_last_negative] = buffer

    return mass

mass = random_array(15, -10, 20)

for i in mass:
    print(str(i)+" ", end='')

print()

new_mass = swap_last_negative_and_first_positive(mass)

for i in new_mass:
    print(str(i)+" ", end='')
