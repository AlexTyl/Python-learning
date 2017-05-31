# В массиве А(N) найти максимальный и минимальный элементы и  переставить их местами


def random_array(dimension, min_element, max_element):
    import random
    mass = []
    while dimension > 0:
        mass.append(random.randint(min_element, max_element))
        dimension -= 1
    return mass


def swap_last_negative_and_first_positive(mass):

    def index_of_max_number(mass):
        current_index = 1
        index_max = 0
        while current_index < len(mass):
            if mass[current_index] > mass[index_max]:
                index_max = current_index
            current_index += 1
        return index_max

    def index_of_min_number(mass):
        current_index = 1
        index_min = 0
        while current_index < len(mass):
            if mass[current_index] < mass[index_min]:
                index_min = current_index
            current_index += 1
        return index_min

    index_of_max_number = index_of_max_number(mass)
    index_min_number = index_of_min_number(mass)

    if index_of_max_number == -1 or index_min_number == -1:
        return mass

    buffer = mass[index_min_number]
    mass[index_min_number] = mass[index_of_max_number]
    mass[index_of_max_number] = buffer
    return mass

mass = random_array(15, -10, 20)

for i in mass:
    print(str(i)+" ", end='')

print()

new_mass = swap_last_negative_and_first_positive(mass)

for i in new_mass:
    print(str(i)+" ", end='')