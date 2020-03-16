import sys
from collections import Counter

ans = []

ss = sys.stdin.readline().strip().upper()
c = Counter(ss)

for k, v in c.items():
    if v == max(c.values()):
        ans.append(k)

        if len(ans) > 1:
            break

if len(ans) > 1:
    print('?')
else:
    print(ans[0])
