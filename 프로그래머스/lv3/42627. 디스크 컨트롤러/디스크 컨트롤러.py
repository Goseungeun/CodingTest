import heapq

def solution(jobs):
    n = len(jobs)
    heapq.heapify(jobs)
    current_time = 0
    heap = []
    answer = 0
    while jobs:
        while jobs:
            start,duration = heapq.heappop(jobs)
            if start > current_time:
                heapq.heappush(jobs,[start,duration])
                break
            else:
                heapq.heappush(heap,[duration,start])
        if len(heap) == 0:
            current_time += 1
        else:
            duration,start = heapq.heappop(heap)
            current_time += duration
            answer += current_time - start
                               
    while heap:
        duration,start = heapq.heappop(heap)
        current_time += duration
        answer += current_time - start
        
    return answer // n