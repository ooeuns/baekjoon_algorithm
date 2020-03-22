import sys

ans = 0


def in_bound(x: int):
    if x >= 0 and x < row:
        return True
    return False


def is_possible(lst: list):
    chk = lst[0]
    for l in lst:
        if l != chk:
            return 0
    return chk[0]


def dfs(idx: int, start: int, lst: list, direction: int):
    if idx - start == K+1:
        return lst[idx]

    if idx < 0 or idx >= len(lst):
        return False

    if lst[idx] == lst[start]:
        return dfs(idx+direction, start, lst, direction)
    else:
        return 0


def is_road(lst: list):
    past = lst[0]
    cnt = 0
    for idx, cur in enumerate(lst):
        if cnt:
            cnt -= 1
            past = cur
            continue

        if past == cur:
            continue
        if past < cur:
            if dfs(0, 0, mtrx[idx-K:idx], -1):
                cnt = dfs(0, 0, mtrx[idx-K:idx], -1)
                continue
        if past > cur:
            if dfs(idx-1, idx-1, mtrx[idx: idx + K + 1], 1):
                cnt = dfs(idx-1, idx-1, mtrx[idx: idx + K + 1], 1)
                continue
        return False
    return True


if __name__ == "__main__":
    row, K = map(int, sys.stdin.readline().split())
    mtrx = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

    for i in range(row):
        if is_road(mtrx[i][:]):
            print(mtrx[i][:])
            print('가로: {} 번째 줄\n'.format(i))
            ans += 1

        tmp = [mtrx[j][i] for j in range(row)]
        if is_road(tmp):
            print(tmp)
            print('세로: {} 번재 줄\n'.format(i))
            ans += 1
    print(ans)
