num = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
ans = sum(map(lambda n: n[0]*n[1], zip(a, b)))

print(ans)