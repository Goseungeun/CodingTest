from collections import deque

def solution(n, computers):
    visit = [0] * n
    cnt = 0
    
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            queue = deque([i])
            while queue:
                com = queue.popleft()
                for j in range(n):
                    if computers[com][j] == 1 and visit[j] == 0:
                        queue.append(j)
                        visit[j] = 1
            cnt += 1
    return cnt