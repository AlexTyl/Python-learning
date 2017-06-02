# В массиве А(N,М) найти максимальный и минимальный элементы  среди  всех  элементов  тех  строк,
# которые  упорядочены  по  возрастанию  или по убыванию.

matrix = [[45, 23, 6, 2, 4, 2, 54, 4],
          [5, 2, 75, 23, 76, 23, 56, 2],
          [-1, 2, 3, 4, 5, 6, 7, 8],
          [43, 23, 76, 4, 87, 23, 56, 1],
          [28, 7, 6, 5, 4, 3, 2, 1],
          [65, 23, 56, 56, 12, 67, 32, 45],
          [54, 2, 65, 1, 7, 1, 4, 1],
          [-3, -1, 6, 7, 45, 46, 234]]


def check_ascending_order(array):
    current_index = 0
    while current_index < len(array) - 1:
        if array[current_index] > array[current_index + 1]:
            return False
        current_index += 1
    return True


def check_descending_order(array):
    current_index = 0
    while current_index < len(array) - 1:
        if array[current_index] < array[current_index + 1]:
            return False
        current_index += 1
    return True


def max_and_min_elements_those_rows_that_ordered(matrix):
    max_and_min = ""
    for i in range(len(matrix)):
        if check_ascending_order(matrix[i]):
            max_and_min += str(i+1) + " row is ascending: max " + str(matrix[i][len(matrix[i]) - 1]) + "; min " \
                           + str(matrix[i][0]) + "\n"
        elif check_descending_order(matrix[i]):
            max_and_min += str(i+1) + " row is descending: max " + str(matrix[i][0]) + "; min " \
                           + str(matrix[i][len(matrix[i]) - 1]) + "\n"
    return max_and_min

print(max_and_min_elements_those_rows_that_ordered(matrix))


