import sys


def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        for j in range(i, len(phone_book)):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                return "NO"
    
    return "YES"

arr = []

t = int(sys.stdin.readline())
for i in range(t): # 테스트 케이스의 개수만큼 반복한다.
    n = int(sys.stdin.readline())
    for j in range(n): # n개의 전화번호를 입력받는다.
        arr.append(sys.stdin.readline())
    print(solution(arr))
    arr.clear()