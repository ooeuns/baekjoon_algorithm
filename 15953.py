import sys


def fir(rank: int):
    if rank == 1:
        return 5000000
    elif rank in (2, 3):
        return 3000000
    elif rank in (4, 5, 6):
        return 2000000
    elif rank in (7, 8, 9, 10):
        return 500000
    elif rank in (11, 12, 13, 14, 15):
        return 300000
    elif rank in (16, 17, 18, 19, 20, 21):
        return 100000
    else:
        return 0


def sec(rank: int):
    if rank == 1:
        return 5120000
    elif rank in (2, 3):
        return 2560000
    elif rank in (4, 5, 6, 7):
        return 1280000
    elif rank in (8, 9, 10, 11, 12, 13, 14, 15):
        return 640000
    elif 16 <= rank and rank <= 31:
        return 320000
    else:
        return 0


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())

        print(fir(a) + sec(b))
