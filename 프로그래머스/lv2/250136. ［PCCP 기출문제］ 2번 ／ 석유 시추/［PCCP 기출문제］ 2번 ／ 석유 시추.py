from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(land):
    visit = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    amt_oil = [0]
    num_oil = 0
    
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] == 1 and visit[i][j] == 0:
                count = 0
                num_oil += 1
                queue = deque()
                queue.append([i,j])
                visit[i][j] = num_oil
                
                while queue:
                    x,y = queue.popleft()
                    count += 1
                    for z in range(4):
                        nx = x + dx[z]
                        ny = y + dy[z]
                        if 0<=nx<len(land) and 0<=ny<len(land[0]):
                            if land[nx][ny] == 1 and visit[nx][ny] == 0:
                                visit[nx][ny] = num_oil
                                queue.append([nx,ny])
                amt_oil.append(count)
    return visit,amt_oil,num_oil

def solution(land):
    visit,amt_oil,num_oil = bfs(land)
    answer = 0
    
    for j in range(len(land[0])):
        sum_oil = 0
        visit_oil = [False] * (num_oil + 1)
        for i in range(len(land)):
            if visit[i][j] != 0 and visit_oil[visit[i][j]] == False:
                sum_oil += amt_oil[visit[i][j]]
                visit_oil[visit[i][j]] = True
        answer = max(answer,sum_oil)
    
    return answer