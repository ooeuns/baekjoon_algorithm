import sys

def solution(numbers):
    numbers.sort(key=lambda x: x*4, reverse=True)
    ans = ''.join(number for number in numbers)  
    return str(int(ans))
    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = list(sys.stdin.readline().split())
    print(solution(numbers))