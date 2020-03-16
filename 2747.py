import sys

d = [0] * 100


def dp(x: int):
    if x <= 2:
        return 1

    global d
    if d[x]:
        return d[x]
    d[x] = dp(x-2) + dp(x-1)

    return d[x]


if __name__ == "__main__":
    x = int(sys.stdin.readline())
    print(dp(x))
