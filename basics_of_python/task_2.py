from operator import add


# (2 Задача) Сумма бинарных чисел
def binary_sum(bin_num1: str, bin_num2: str) -> str:
    """Adds two binary numbers"""
    return bin(int(bin_num1, 2) + int(bin_num2, 2))[2:]


# Реализация алгоритма конвертирования числа из бинарного в десятичное
def convert_binary_to_decimal(binary_num: str) -> int:
    digits_of_number = len(binary_num) - 1
    decimal_num = 0

    for item in binary_num:
        decimal_num += int(item) * 2 ** digits_of_number
        digits_of_number -= 1

    return decimal_num


# Реализация алгоритма конвертирования числа из десятичного в бинарное
def convert_decimal_to_binary(decimal_num: int) -> str:
    division = decimal_num
    rests_of_division = ''

    while division != 0:
        rests_of_division += str(division % 2)
        division = division // 2

    binary_num = rests_of_division[::-1]
    return binary_num


# Собственная реализация сложения двоичных чисел
def binary_sum2(binary_num_one: str, binary_num_two: str) -> str:
    '''Калькулятор бинарных чиcел'''
    result = add(
        convert_binary_to_decimal(binary_num_one),
        convert_binary_to_decimal(binary_num_two),
    )
    return convert_decimal_to_binary(result)
