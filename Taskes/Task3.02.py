# В  массиве  А(N,М)  найти  номер  строки,
# среднее  арифметическое  положительных элементов которой является наименьшим.


def creation_random_matrix(dimension_N, dimension_M, min_element, max_element):
    import random
    matrix = []
    current_element = dimension_N
    while current_element > 0:
        matrix.append([])
        current_element -= 1
    while current_element < len(matrix):
        for i in range(dimension_M):
            matrix[current_element].append(random.randint(min_element, max_element))
        current_element += 1
    return matrix


def arithmetic_mean_positive_elements(array):
    positive_counter = 0
    positive_sum = 0
    for i in array:
        if i > 0:
            positive_sum += i
            positive_counter += 1
    if positive_counter > 0:
        return positive_sum / positive_counter
    return 0


def index_of_min_number(mass):
    current_index = 1
    index_min = 0
    while current_index < len(mass):
        if mass[current_index] < mass[index_min]:
            index_min = current_index
        current_index += 1
    return index_min


def row_with_least_arithmetic_mean(matrix):
    array_arithmetic_mean = []
    for i in range(len(matrix)):
        array_arithmetic_mean.append(arithmetic_mean_positive_elements(matrix[i]))
    return index_of_min_number(array_arithmetic_mean) + 1

matrix = creation_random_matrix(5, 7, -10, 20)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(str(matrix[i][j]) + " ",  end='')
    print()

print("Line with the least arithmetic mean: " + str(row_with_least_arithmetic_mean(matrix)))