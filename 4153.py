def solution(triangle):
    triangle.sort()
    if (triangle[0] ** 2) + (triangle[1] ** 2) == triangle[2] ** 2:
        return "right"
    else:
        return "wrong"


if __name__ == "__main__":
    while True:
        triangle = list(map(int, input().split()))
    
        if sum(triangle) == 0:
            break
        print(solution(triangle))
