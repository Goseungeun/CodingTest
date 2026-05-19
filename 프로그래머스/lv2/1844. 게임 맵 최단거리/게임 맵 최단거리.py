from collections import deque

def solution(maps):
    queue = deque()
    queue.append([0,0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while queue:
        x, y = queue.popleft()
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return maps[x][y]
        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]
            if (0 <= next_x < len(maps)) and (0 <= next_y < len(maps[0])):
                if maps[next_x][next_y] == 1:
                    queue.append([next_x, next_y])
                    maps[next_x][next_y] = maps[x][y]+1
    return -1