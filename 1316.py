import sys
from collections import deque


def group_word(words):
    usage = set()
    check = words[0]
    for word in words:
        if word in usage:
            return False
        if check == word:
            continue
        else:
            usage.add(check)
            check = word
    return True


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    count = 0
    for _ in range(N):
        words = sys.stdin.readline().strip()
        if group_word(words):
            count += 1
    print(count)
