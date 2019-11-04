keyword = input()

row, col = tuple(map(int, input().split()))

board = []
for _ in range(row):
    board.append(input())


deltas = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]


def find(r, c, delta):
    idx = 0
    dr, dc = delta
    while idx < len(keyword):
        if not (0 <= r < row and 0 <= c < col):
            return False
        if keyword[idx] == board[r][c]:
            idx += 1
            r, c = r + dr, c + dc
        else:
            return False

    return True


def solution():
    for r in range(row):
        for c in range(col):
            for delta in deltas:
                if find(r, c, delta):
                    return 1
    return 0