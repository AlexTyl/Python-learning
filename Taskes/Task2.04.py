# В  массиве  А(N)  найти  количество  пар  одинаковых  соседних элементов.


def random_array(dimension, min_element, max_element):
    import random
    mass = []
    while dimension > 0:
        mass.append(random.randint(min_element, max_element))
        dimension -= 1
    return mass


def number_of_identical_pairs(mass):
    number_identical_pairs = 0
    current_index = 0
    while current_index < len(mass) - 1:
        if mass[current_index] == mass [current_index + 1]:
            number_identical_pairs += 1
        current_index += 1
    return number_identical_pairs


mass = random_array(15, -10, 20)

for i in mass:
    print(str(i)+" ", end='')

print()

print(number_of_identical_pairs(mass))