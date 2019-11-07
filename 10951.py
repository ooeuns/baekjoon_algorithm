while True:
    try:
        numbers = list(map(int, input().split()))
        print(sum(numbers))
    except:
        break