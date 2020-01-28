import sys


T = int(sys.stdin.readline())

for _ in range(T):
    country, plane = map(int,  sys.stdin.readline().split())
    for _ in range(plane):
        x, y = map(int,  sys.stdin.readline().split())
    print(country-1)
    