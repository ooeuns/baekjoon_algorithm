import sys

move = []

def hanoi(num: int, start: int, to: int, other: int):
    if not num:
        return
    hanoi(num-1, start, other, to)
    print('{}번에서 {}로 옮긴다.'.format(start, to))
    hanoi(num-1, other, to, start)

hanoi(4, 0, 1, 2)