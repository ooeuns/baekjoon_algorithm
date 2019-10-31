import sys


def solution(people):
    N = len(people)
    count = 0

    for start in  range(N-1):
        most_tall = float('-inf')
        for end in range(start+1, N):
            if people[start] >= most_tall and people[end] >= most_tall:
                # print("{}-{}".format(people[start], people[end]))
                count += 1
            if most_tall < people[end]:
                most_tall = people[end]
            # most_tall = max(people[start:end+1])
    return count
            
if __name__ == "__main__":
    # N = int(sys.stdin.readline())
    # people = [int(sys.stdin.readline()) for _ in range(N)]
    # print(solution(people))

    print(solution([2, 4, 1, 2, 2, 5, 1]))    
