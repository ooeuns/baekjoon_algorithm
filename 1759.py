import sys
from itertools import combinations

VOWEL = set(['a', 'e', 'i', 'o', 'u'])


def za_mo(word: list):
    return len(VOWEL & set(word)) >= 1 and len(set(word) - VOWEL) >= 2


def solution(l: int, alphabet: list):
    return sorted(list(map(''.join, map(sorted, filter(za_mo, list(combinations(alphabet, l)))))))


if __name__ == "__main__":
    l, c = map(int, sys.stdin.readline().split())
    alphabet = list(sys.stdin.readline().split())

    for ans in solution(l, alphabet):
        print(ans)
