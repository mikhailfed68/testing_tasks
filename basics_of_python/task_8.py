from itertools import chain


def is_happy_ticket(ticket):
    center = len(ticket) // 2
    number = tuple(chain(ticket))
    return sum(number[:center]) == (number[center:])
