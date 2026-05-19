from collections import deque

def bfs(visit, graph):
    queue = deque((1))
    # queue.append(1)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                queue.append(i)
                visit[i] = visit[x] + 1
    return visit
    

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    visit = [0] * (n+1)
    visit[1] = 1
    visit = bfs(visit, graph)
    
    return visit.count(max(visit))