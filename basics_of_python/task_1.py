# (1 Задача) Фибонначи
def fib_2(n):
    """Calculaties a number of Fibbonachi"""
    if n == 0 or n == 1:
        return n

    counter = 1
    last_values = [0, 1]
    while counter != n:
        res = last_values[0] + last_values[1]
        last_values.pop(0)
        last_values.append(res)
        counter += 1
    return res
