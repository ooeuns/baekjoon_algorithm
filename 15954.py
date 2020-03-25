import sys
import math
from decimal import Decimal

ans = Decimal('inf')


N, K = map(int, sys.stdin.readline().split())
dolls = list(map(int, sys.stdin.readline().split()))

for i in range(N-K+1):
    sum_val = sum(dolls[i:i+K-1])
    sum_val_sq = sum(map(lambda x: x ** 2, dolls[i:i+K-1]))

    for j in range(K, N-i+1):
        sum_val += dolls[i+j-1]
        sum_val_sq += dolls[i+j-1] ** 2
        aver = sum_val / Decimal(j)
        std = (sum_val_sq / Decimal(j) - aver ** 2).sqrt()

        ans = min(ans, std)

print(ans)
