import sys

def solve(a):
    return sum(a)

if __name__ == "__main__":
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(a))