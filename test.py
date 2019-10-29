import sys
from functools import cmp_to_key

def solution(numbers):
    # numbers.sort(key=lambda x: x*4, reverse=True)
    numbers.sort(key=cmp_to_key())
    ans = ''.join(number for number in numbers)  
    return str(int(ans))
    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = list(sys.stdin.readline().split())
    print(solution(numbers))