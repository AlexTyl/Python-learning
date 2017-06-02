# В  массиве  А(N,N)  найти  суммы  элементов,  расположенных  на  главной диагонали, ниже диагонали и выше диагонали.


def creation_square_matrix(dimension, min_element, max_element):
    import random
    matrix = []
    current_element = dimension
    while current_element > 0:
        matrix.append([])
        current_element -= 1
    while current_element < len(matrix):
        for i in range(dimension):
            matrix[current_element].append(random.randint(min_element, max_element))
        current_element += 1
    return matrix


def sum_elements_main_diagonal(matrix):
    sum_elements = 0
    for i in range(len(matrix)):
        sum_elements += matrix[i][i]
    return sum_elements


def sum_elements_above_main_diagonal(matrix):
    sum_elements = 0
    for i in range(len(matrix) - 1):
        j = i + 1
        while j < len(matrix):
            sum_elements += matrix[i][j]
            j += 1
    return sum_elements


def sum_elements_under_main_diagonal(matrix):
    sum_elements = 0
    for i in range(len(matrix) - 1):
        j = i + 1
        while j < len(matrix):
            sum_elements += matrix[j][i]
            j += 1
    return sum_elements

matrix = creation_square_matrix(5, -10, 20)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(str(matrix[i][j]) + " ",  end='')
    print()

print("Sum of elements of the main diagonal: " + str(sum_elements_main_diagonal(matrix)))
print("The sum of the elements under the main diagonal: " + str(sum_elements_above_main_diagonal(matrix)))
print("The sum of the elements above the main diagonal: " + str(sum_elements_under_main_diagonal(matrix)))