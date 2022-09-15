# (3 Задача) Физзбазз
def fizz_buzz(begin: int, end: int) -> str:
    res = []

    for num in range(begin, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            res.append('FizzBuzz')
        elif num % 3 == 0:
            res.append('Fizz')
        elif num % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(num))

    return ' '.join(res)
