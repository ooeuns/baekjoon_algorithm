from collections import deque
import copy
import sys


direction = [
    (1, 1),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
    (1, -1),
    (-1, -1),   
    ]


def has_word(y, x, word, dirc, place, length):

    dy, dx = dirc
    if not word: return True    # word를 다 찾았다면 존재한다면
    if not (0 <= y < length and 0 <= x < length): return False   # 범위를 벗어난다면

    if place[y][x] == word[0]:
        word.popleft()
        w = copy.deepcopy(word)
        if has_word(y+dy, x+dx, w, dirc, place, length):
            return True


def solution(place, word, height, width, length):
    for y in range(height):
        for x in range(width):
            for dirc in direction:
                w = copy.deepcopy(word)
                if has_word(y, x, w, dirc, place, length):
                    return 1
    return 0
    
if __name__ == "__main__":
    word = deque(sys.stdin.readline().strip())
    width, height = map(int, sys.stdin.readline().split())
    place = [sys.stdin.readline().strip() for _ in range(height)]
    print(solution(place, word, height, width, len(word)))
    
    # print(solution(["ACDBE", "ABCED", "ACCEE", "ACHDF", "ACBCE"], deque("ABCD"), 5, 5, 4))
            



    