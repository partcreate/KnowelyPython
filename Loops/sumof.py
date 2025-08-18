
def sum_of(number_1, number_2):

    if number_1 > number_2:
        number_1, number_2 = number_2, number_1

    return sum(range(number_1, number_2 + 1))


print(sum_of(1240, -1250))