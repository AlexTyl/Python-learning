# Дан массив А(N). Получить массив В(N),
# i-элемент которого равен  среднему арифметическому первых i элементов массива  А.


def random_array(dimension, min_element, max_element):
    import random
    mass = []
    while dimension > 0:
        mass.append(random.randint(min_element, max_element))
        dimension -= 1
    return mass


def arithmetical_mean_by_index(mass, arithmetical_index):
    summ = 0
    current_index = 0
    while current_index <= arithmetical_index:
        summ += mass[current_index]
        current_index += 1
    return summ / (arithmetical_index+1)


def new_mass_arithmetical_by_old_mass(old_mass):
    new_mass = []
    current_index = 0
    while current_index < len(old_mass):
        new_mass.append(arithmetical_mean_by_index(old_mass, current_index))
        current_index += 1
    return new_mass


old_mass = random_array(15, -10, 20)

for i in old_mass:
    print(str(i)+" ", end='')

print()

new_mass = new_mass_arithmetical_by_old_mass(old_mass)

for i in new_mass:
    print(str(i)+" ", end='')