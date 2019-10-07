def solution(K):
    lst = []
    while K:
        num = int(input())
        if num != 0:
            lst.append(num)
        else:
            lst.pop()
        K -= 1
    return sum(lst)

if __name__ == "__main__":
    K = int(input())
    print(solution(K))
