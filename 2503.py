import sys
from itertools import permutations

def judge_strike(ans_num: str, qst_num: str):
    strike = 0
    for idx in range(3):
        if ans_num[idx] == qst_num[idx]:
            strike += 1
    return strike

def judge_ball(ans_num: str, qst_num: str):
    ball = 0
    for idx in range(3):
        if qst_num[idx] in ans_num:
            ball += 1
    return ball - judge_strike(ans_num, qst_num)

def solution(baseball):
    number_of_cases = set(''.join(idx) for idx in permutations("123456789", 3))

    for rounds in baseball:
        qst_num, strike, ball = rounds
        qst_num = str(qst_num)

        difference = set()
        for ans_num in number_of_cases:
            if strike != judge_strike(ans_num, qst_num) or ball != judge_ball(ans_num, qst_num):
                difference.add(ans_num)
                continue
        if difference:
            number_of_cases = number_of_cases - difference
    return len(number_of_cases)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    baseball = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution(baseball))
    # print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))