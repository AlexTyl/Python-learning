# Вычислить значение многочлена и всех его производных в заданной точке x (коэффициенты хранятся в массивах ).


def random_array(dimension, min_element, max_element):
    import random
    mass = []
    while dimension > 0:
        mass.append(random.randint(min_element, max_element))
        dimension -= 1
    return mass


def creating_polynomial(array, x):
    polynomial = ""
    derivative = ""
    power = len(array) - 1
    index = 0
    value_of_polynomial = 0
    values_individual_derivative = []
    while power >= 0:
        polynomial = polynomial + " + (" + str(array[index]) + " * " + str(x) + "^" + str(power) + ")"
        value_of_polynomial += array[index] * x ** power
        if power > 0:
            derivative = derivative + " + (" + str(power*array[index]) + " * " + str(x) + "^" + str(
                power - 1) + ")"
            values_individual_derivative.append(power * array[index])
        power -= 1
        index += 1
    print(polynomial[3:len(polynomial)] + "\nThe value of a polynomial: " + str(value_of_polynomial))
    print("Polynomial derivative: " + derivative[3:len(derivative)])
    print("=====================================================")
    if len(values_individual_derivative) > 0:
        return creating_polynomial(values_individual_derivative, x)
    return 0

print("Enter number of elements of a polynomial: ")
number_of_elements = int(input())

print("Enter x: ")
x = int(input())

array = random_array(number_of_elements, -10, 20)

for i in array:
    print(str(i)+" ", end='')

print()
print()

creating_polynomial(array, x)