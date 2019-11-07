N = int(input())

for _ in range(N):
    num, sentence = input().split()
    num = int(num)
    ans = []
    for s in sentence:
        ans.append(s * num)
    print(''.join(ans))