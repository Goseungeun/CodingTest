import heapq

def solution(n, s, a, b, fares):  
    answer = float('inf')
    graph = [[] for _ in range(n+1)]
    
    for f in fares:
        graph[f[0]].append([f[1], f[2]])
        graph[f[1]].append([f[0], f[2]])
    
    def search(cost, start):
        # nonlocal graph
        cost[start] = 0
        q = []
        heapq.heappush(q, (start, 0))

        while q:
            cur, cur_cost = heapq.heappop(q)
            if cost[cur] < cur_cost:
                continue

            for node, dis in (graph[cur]):
                if cur_cost + dis < cost[node]:
                    cost[node] = cur_cost + dis
                    heapq.heappush(q, (node, cur_cost+dis))
        return cost
    
    INF = float("inf")
    cost_s = [INF]*(n+1)
    cost_a = [INF]*(n+1)
    cost_b = [INF]*(n+1)
    
    cost_s = search(cost_s, s)
    cost_a = search(cost_a, a)
    cost_b = search(cost_b, b)
    
    for k in range(1, n+1):
        answer = min(cost_s[k]+cost_a[k]+cost_b[k], answer)
    
    if answer > cost_s[a]+cost_s[b]:
        answer = cost_s[a]+cost_s[b]
    
    return answer