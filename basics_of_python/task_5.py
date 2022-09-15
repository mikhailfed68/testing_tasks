# (Задача 5) Вращение троек (элементов кортежа)
def rotate_left(value: tuple) -> tuple:
    queue = list(value)
    queue.append(queue.pop(0))
    return tuple(queue)


def rotate_right(value: tuple) -> tuple:
    queue = list(value)
    queue.insert(0, queue.pop())
    return tuple(queue)
# OR result = (values[2], values[0], values[1])
