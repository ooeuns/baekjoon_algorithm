import sys
from collections import deque, Counter
from itertools import permutations

ans = float('-inf')
visited = [False] * 10


def sum_words(number: str, words: list, set_alpha: set):
    # print('set_alpha: {}'.format(set_alpha))    # debug
    # print('number: {}'.format(number))    # debug

    package = {a: n for a, n in zip(set_alpha, number)}
    result = []

    for word in words:
        convert = ''
        # print(word[0])   # debug
        # print(package)
        # print(package[word[0]])   # debug

        for w in word:
            # # debug
            # print('w: {}'.format(w))    # debug
            # print('package: {}'.format(package))    # debug
            # print('package[w]: {}'.format(package[w]))  # debug

            convert += package[w]
        result.append(int(convert))

    return sum(result)


def backTracking(number: str, idx: int, words: list, set_alpha: set):
    global ans, visited

    if idx == len(set_alpha):
        ans = max(ans, sum_words(number, words, set_alpha))
        # TODO 기저사례
        # 현재 까지의 number로 wrods를 모두 숫자로 바꾼 후 sum값을 출력하는 함수 필요.
        return

    cnt = 0
    for i in range(9, length, -1):
        if cnt > SQRT:
            break
        if not visited[i]:
            cnt += 1

            visited[i] = True
            backTracking(number + str(i), idx+1, words, set_alpha)
            visited[i] = False


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    words = []
    set_alpha = set()

    # 사용한 알파벳 집합과 단어숫자 리스트를 만듦.
    for _ in range(N):
        w = sys.stdin.readline().strip()

        words.append(w)
        set_alpha.update(set(w))

    # 사용할 숫자의 길이
    length = 9 - len(set_alpha)

    # sqrt
    SQRT = int(len(set_alpha) ** 0.5)

    # 9부터 length까지 백트래킹: 첫번째 값 넣기
    for i in range(9, SQRT, -1):
        visited[i] = True
        backTracking(str(i), 1, words, set_alpha)
        visited[i] = False

    print(ans)
