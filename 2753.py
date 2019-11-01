def solution(year):
    # 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때 이다.
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return 1
    return 0

if __name__ == "__main__":
    year = int(input())
    print(solution(year))