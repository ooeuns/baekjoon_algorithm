from collections import deque


AROUND = ((-1, 0), (0, 1), (1, 0), (0, -1))

# create map
row, col, A, B, K = map(int, input().split())
maps = [[1] * col for _ in range(row)]
dist = [[0] * col for _ in range(row)]

# create unit
size = (A, B)

# create obstacle
for _ in range(K):
    y, x = map(int, input().split())
    maps[y][x] = 0

# start, end points
start = list(map(int, input().split()))
end = list(map(int, input().split()))

class Unit:
    def __init__(self, size):
        self.start_y, self.start_x = start
        self.size_y, self.size_x = size
        self.current_location = [[self.start_y, self.start_x]]
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.current_location.append([self.start_y - y, self.start_x - x])
    
    def is_arrive(self):
        for location in self.current_location:
            if end in location:
                return dist[self.next_y][self.next_y]

    def move(self, dy, dx):
        for location in self.current_location:
            self.y, self.x = location
            self.next_y = self.y + dy
            self.next_x = self.x + dx

            # check bounds
            if not (0 <= self.next_y < row and 0 <= self.next_x < col):
                return False
            
            # check obstacle
            if not maps[self.next_y][self.next_x]:
                return False
        
        # moving
        for idx, location in enumerate(self.current_location):
            self.y, self.x = location
            self.next_y = self.y + dy
            self.next_x = self.x + dx

            # record distance
            dist[self.next_y][self.next_x] = dist[self.y][self.x] + 1

            # move unit
            self.current_location[idx][0] = self.next_y
            self.current_location[idx][1] = self.next_x
        return True

def game():
    unit = Unit(size)
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        for dy, dx in AROUND:
            if unit.move(dy, dx):
                queue.append((y+dy, x+dx))

            if unit.is_arrive():
                return unit.is_arrive()

if __name__ == "__main__":
    print(game())
    print(dist) # debug

# 5 5 2 2 3
# 2 2
# 3 2
# 3 3
# 4 1
# 1 4