N = int(input())
for _ in range(N):
    quiz = input()
    ans = 0
    count = 0
    for q in quiz:
        if q == 'O':
            count += 1
            ans += count
        else:
            count = 0
    print(ans)
