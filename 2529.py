import sys

visited = [False] * 10
max_num, min_num = '', '9999999999'


def is_possible(i: str, j: str, k: str):
    if k == '<':
        return i < j
    elif k == '>':
        return i > j


def backTracking(selected: str, idx: int):
    global min_num
    global max_num

    if idx == N:
        if selected < min_num:
            min_num = selected
        else:
            max_num = selected
    else:
        for i in range(10):
            if not visited[i] and is_possible(selected[-1], str(i), inqu[idx]):
                visited[i] = True
                backTracking(selected + str(i), idx+1)
                visited[i] = False


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    inqu = list(sys.stdin.readline().strip().split())

    for first_num in range(10):
        visited[first_num] = True
        backTracking(str(first_num), 0)
        visited[first_num] = False

    print(max_num)
    print(min_num)
