AROUND = ((-1, 0), (0, 1), (1, 0), (0, -1))

# create map
row, col = map(int, input().split())
maps = [[1] * col for _ in range(row)]

# create unit
unit = tuple(map(int, input().split()))

# create obstacle
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    maps[y][x] = 0

# start, end points
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

class Unit:
    def __init__(self, size):
        self.start_y, self.start_x = start
        self.size_y, self.size_x = size
        self.current_location = [[self.start_y, self.start_x]]
        for y in range(1, self.size_y+1):
            for x in range(1, self.size_x+1):
                self.current_location.append([self.start_y + y, self.start_x + x])
    
    def is_arrive(self):
        for location in self.current_location:
            if end in location:
                return True
