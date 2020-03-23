import sys


def rotate(lst: list):
    return list(zip(*lst[::-1]))


def count_sticker(lst: list):
    ans = 0
    for l in lst:
        ans += l.count(1)
    return ans


def in_bounds(y: int, x: int):
    if (y >= 0 and y <= row) and (x >= 0 and x <= col):
        return True
    return False


def chk_area(mac_y: int, mac_x: int, package: tuple):
    dy, dx, sticker = package

    for y in range(dy):
        for x in range(dx):

            if sticker[y][x] == 1 and mac_book[mac_y+y][mac_x+x] == 1:
                return False
    return True


def attach_sticker(mac_y: int, mac_x: int, package: tuple):
    dy, dx, sticker = package
    for y in range(dy):
        for x in range(dx):
            if mac_book[mac_y+y][mac_x+x] == 0 and sticker[y][x]:
                mac_book[mac_y+y][mac_x+x] = 1


def solution(package: tuple):
    dy, dx, sticker = package
    cnt = 0

    while True:
        for y in range(row):
            for x in range(col):

                if not in_bounds(dy+y, dx+x):
                    break
                if chk_area(y, x, package):
                    attach_sticker(y, x, package)
                    return

        if cnt == 3:
            return

        sticker = rotate(sticker)
        dy, dx = dx, dy
        package = (dy, dx, sticker)
        cnt += 1


if __name__ == "__main__":
    row, col, k = map(int, sys.stdin.readline().split())
    mac_book = [[0] * col for _ in range(row)]

    stickers = []
    for _ in range(k):
        paper_r, paper_c = map(int, sys.stdin.readline().split())
        sticker = [list(map(int, sys.stdin.readline().split()))
                   for _ in range(paper_r)]
        stickers.append((paper_r, paper_c, sticker))

    for package in stickers:
        solution(package)

    print(count_sticker(mac_book))
