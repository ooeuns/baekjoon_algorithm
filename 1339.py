import sys


def solution(words: list, alphabet: list):
    ans = 0

    for word in words:
        i = 0
        while word:
            now = word[-1]
            alphabet[ord(now) - ord('A')] += 10 ** i
            i += 1
            word = word[:-1]

    alphabet.sort(reverse=True)
    for i in range(10):
        ans += alphabet[i] * (9 - i)

    return ans


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    alphabet = [0] * 26

    words = [sys.stdin.readline().strip() for _ in range(T)]
    print(solution(words, alphabet))
