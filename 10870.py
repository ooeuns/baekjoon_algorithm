def  fibonacci(N):
    if not N: return 0
    return 1 if N <3 else fibonacci(N-1) + fibonacci(N-2)
print(fibonacci(int(input())))