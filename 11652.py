import sys
import collections

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]

counter = dict(collections.Counter(num))
ans = sorted(counter.items(), reverse=True, key=lambda n: (n[1], -n[0]))

print(ans[0][0])