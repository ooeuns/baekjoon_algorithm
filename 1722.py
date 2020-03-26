import sys

cache = {}


def factorial_recursive(n):
    global cache

    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1
    else:
        cache[n] = n * factorial_recursive(n-1)
        return cache[n]


def one_solution(k: int):
    ans = []

    for i in range(N):
        x = factorial_recursive(N-1-i)
        step = (k-1) // x
        ans.append(numbers[step])
        numbers.remove(numbers[step])
        k -= x * step
    return ans


def two_solution(permu: list):
    ans = 1
    sort_permu = sorted(permu)

    for i in range(N):
        step = sort_permu.index(permu[i])
        sort_permu.remove(permu[i])
        x = factorial_recursive(N-1-i)
        ans += x * step
    return ans


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    small_q = list(map(int, sys.stdin.readline().split()))

    numbers = [x for x in range(1, N+1)]

    if small_q[0] == 1:
        print(*one_solution(small_q[1]))
    else:
        print(two_solution(small_q[1:]))
