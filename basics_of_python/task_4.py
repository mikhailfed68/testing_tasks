# (4 Задача) Классификация отрезков
def is_degenerated(line):
    p1, p2 = line
    return p1 == p2


def is_vertical(line):
    p1, p2 = line
    return p1[1] == p2[1] and not is_degenerated(line)


def is_horizontal(line):
    p1, p2 = line
    return p1[0] == p2[0] and not is_degenerated(line)


def is_inclined(line):
    return (
        not is_vertical(line)
        and not is_horizontal(line)
        and not is_degenerated(line)
    )
