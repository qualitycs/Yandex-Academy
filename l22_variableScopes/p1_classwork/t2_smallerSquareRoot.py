def discriminant(a, b, c):
    return b * b - 4 * a * c


def larger_root(p, q):
    d = discriminant(1, p, q)
    return (-p + d ** 0.5) / 2


def smaller_root(p, q):
    d = discriminant(1, p, q)
    return (-p - d ** 0.5) / 2


def main():
    seed = float(input())
    cope = float(input())
    print(discriminant(1, seed, cope))
    print(smaller_root(seed, cope), larger_root(seed, cope))
