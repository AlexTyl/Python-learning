# В массиве А(N,М) найти сумму элементов тех столбцов, все элементы которых кратны заданному числу р.


def sum_elements_columns_multiples(matrix, p):
    sum = 0
    cols_multiples_array = []
    for j in range(len(matrix[0])):
        col_multiples = True
        for i in range(len(matrix)):
            if matrix[i][j] % p != 0:
                col_multiples = False
                break
        if col_multiples:
            cols_multiples_array.append(j)
    for j in cols_multiples_array:
        for i in range(len(matrix)):
            sum += matrix[i][j]
    return sum

print("Enter the p-number: ")
p = int(input())

matrix = \
[[16,     12,      3,     3,    -2,     5,     6,     -1,    -10,     6],
[ 15,     -8,     -1,    -3,     0,     15,     2,    -10,      4,     3],
[  7,    -10,     -8,    -9,     6,    -25,    12,      8,     -2,    -9],
[ -7,      9,      3,   -12,   -10,    10,    16,      8,     11,    15],
[ 14,     14,      7,    15,    -6,   -15,    12,     15,     -9,    21]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(str(matrix[i][j]) + "      ",  end='')
    print()

print(sum_elements_columns_multiples(matrix, p))