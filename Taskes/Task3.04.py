# В  массиве А(N,М) найти сумму тех элементов, в записи которых  используются только цифры 0, 1, 3, 8.


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


def check_valid_number(number):
    number = abs(number)
    while number != 0:
        if number % 10 in [2, 4, 5, 6, 7, 9]:
            return False
        number //= 10
    return True


def sum_valid_number(matrix):
    valid_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if check_valid_number(matrix[i][j]):
                valid_sum += matrix[i][j]
    return valid_sum

matrix = creation_random_matrix(5, 7, -10, 20)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(str(matrix[i][j]) + " ",  end='')
    print()

print("Sum of valid numbers is: " + str(sum_valid_number(matrix)))