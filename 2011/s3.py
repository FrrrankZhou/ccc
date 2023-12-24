T = int(input())
base = ((1, 0), (2, 0), (3, 0), (2, 1))


def is_crystal(m, x, y) -> bool:
    if m == 1:
        if (x, y) in base:
            return True
        else:
            return False
    if is_crystal(m - 1, x // 5, y // 5):
        return True
    elif is_crystal(m - 1, x // 5, (y // 5) - 1) and (x % 5, y % 5) in base:
        return True
    else:
        return False


for _ in range(T):
    M, X, Y = map(int, input().split())
    if is_crystal(M, X, Y):
        print('crystal')
    else:
        print('empty')
