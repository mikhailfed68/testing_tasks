# (Задача 6) Поиск наименьшей разницы углов
def diff(angle1, angle2=0):
    max_angle = max(angle1, angle2)
    min_angle = min(angle1, angle2)
    difference1 = max_angle - min_angle

    return abs(
        difference1 if difference1 <= 180
        else (360 - max_angle) + min_angle
    )
