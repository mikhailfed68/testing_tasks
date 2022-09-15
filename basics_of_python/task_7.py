from math import log


# (Задача 7) Степени тройки
def is_power_of_three(num):
    return True if int(log(num, 3)) != 0 or num == 1 else False
