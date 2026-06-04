import heapq

def solution(operations):
    answer = []
    hq = []
    
    for operation in operations:
        alpha , num  = operation.split()
        num = int(num)
        if alpha == "I":
            heapq.heappush(hq,num)
        else:
            if hq:
                if num == -1:
                    heapq.heappop(hq)
                else:
                    hq.sort()
                    hq.pop()
                    
    hq.sort()
    if hq:
        answer = [hq[-1],hq[0]]
    else:
        answer = [0,0]
    return answer