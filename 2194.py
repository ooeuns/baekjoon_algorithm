from collections import deque


# initialization
AROUND = ((-1, 0), (0, 1), (1, 0), (0, -1))

# create map
row, col, A, B, K = map(int, input().split())
maps = [[1] * col for _ in range(row)]
dist = [[0] * col for _ in range(row)]
visited = [[0] * col for _ in range(row)]

# create unit
size = (A, B)

# create obstacle
for _ in range(K):
    y, x = map(int, input().split())
    maps[y-1][x-1] = 0

# start, end points
start = list(map(lambda x: int(x)-1, input().split()))
end = list(map(lambda x: int(x)-1, input().split()))

visited[start[0]][start[1]] = 1


class Unit:
    def __init__(self, size):
        self.start_y, self.start_x = start
        self.size_y, self.size_x = size
        self.current_location = []
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.current_location.append([(self.start_y) + y, (self.start_x) + x])

    def initialization(self):
        for location in self.current_location:
            if not maps[location[0]][location[1]]:
                return False

    def is_arrive(self):
        location = self.current_location[0]
        if end == location:
            self.end_y, self.end_x = end
            return dist[self.end_y][self.end_x]

    def move(self, dy, dx):
        # unit size 전체 check
        for location in self.current_location:
            self.y, self.x = location
            self.next_y = self.y + dy
            self.next_x = self.x + dx

            # check bounds
            if not (0 <= self.next_y < row and 0 <= self.next_x < col):
                return False
            
            # print("next_y: ", self.next_y, "self_x: ", self.next_x)
            # print("maps: ", maps[self.next_y][self.next_x])

            # check obstacle
            if not maps[self.next_y][self.next_x]:
                return False

        
        self.y, self.x = self.current_location[0]
        self.next_y = self.y + dy
        self.next_x = self.x + dx

        # check visited
        if visited[self.next_y][self.next_x]:
            return False

        # record distance
        dist[self.next_y][self.next_x] = dist[self.y][self.x] + 1
        visited[self.next_y][self.next_x] = 1        
        
        # moving
        for idx, location in enumerate(self.current_location):
            self.y, self.x = location
            self.next_y = self.y + dy
            self.next_x = self.x + dx

            # print(dist) # debug

            # move unit
            self.current_location[idx][0] = self.next_y
            self.current_location[idx][1] = self.next_x
        # print(self.current_location)    # debug
        return True

def game():
    unit = Unit(size)
    if not unit.initialization:
        return -1
    queue = deque([start])

    while queue:
        y, x = queue.popleft()
        for dy, dx in AROUND:
            if unit.move(dy, dx):
                queue.append([y+dy, x+dx])
                if unit.is_arrive():
                    return unit.is_arrive()
    return -1

if __name__ == "__main__":
    print(game())

