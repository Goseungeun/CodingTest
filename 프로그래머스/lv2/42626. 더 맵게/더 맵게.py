import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    for _ in range(len(scoville)):
        x = heapq.heappop(scoville)
        if x >= K:
            return answer
        elif len(scoville) == 0:
            return -1
        else:
            y = heapq.heappop(scoville)
            heapq.heappush(scoville,x+2*y)
            answer += 1
