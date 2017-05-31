# В массиве  А(N)  найти:
# а) число  элементов,  предшествующих  первому отрицательному элементу;
# б) сумму нечетных элементов массива, следующих за последним отрицательным элементом.


def random_array(dimension, min_element, max_element):
    import random
    mass = []
    while dimension > 0:
        mass.append(random.randint(min_element, max_element))
        dimension -= 1
    return mass


def before_first_negative_number(mass):
    for current_index in range(len(mass)):
        if mass[current_index] < 0:
            return "a) " + str(current_index)
    return "a) There are no negative numbers in the array"


def index_of_last_negative_number(mass):
    current_index = len(mass) - 1
    while current_index > 0:
        if mass[current_index] < 0:
            return current_index
        current_index -= 1
    return -1


def i_have_no_idea_how_to_call_this_function(mass):
    current_element = index_of_last_negative_number(mass)
    if current_element == -1:
        return "b) There are no negative numbers in the array"
    elif current_element == len(mass) - 1:
        return "b) No elements after the last negative"
    current_element += 1
    summ_odd_numbers = 0
    while current_element < len(mass):
        if mass[current_element] % 2 != 0:
            summ_odd_numbers += mass[current_element]
        current_element += 1
    return "b) " + str(summ_odd_numbers)


mass = random_array(15, -10, 20)

for i in mass:
    print(str(i)+" ", end='')

print()

print(before_first_negative_number(mass))
print(i_have_no_idea_how_to_call_this_function(mass))