import sys

abc = [int(sys.stdin.readline()) for _ in range(3)]
nums = str(abc[0] * abc[1] * abc[2])
check = [0] * 10

for num in nums:
    check[int(num)] += 1
for c in check:
    print(c)