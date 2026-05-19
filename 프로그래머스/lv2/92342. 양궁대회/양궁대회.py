from collections import deque

def bfs(n,info):
    res = []  #최대 점수 차를 내는 화살 상황 저장
    q = deque([(0,[0,0,0,0,0,0,0,0,0,0,0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n: #종료조건 : 화살 다 쓴 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i]==0 and arrow[i] ==0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(arrow)
    
        elif sum(arrow) > n :
            continue
        
        elif focus == 10:
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1,tmp))
            
        else:
            tmp = arrow.copy()
            tmp[focus] = info[focus] +1
            q.append((focus+1,tmp))
            
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))
    return res

def solution(n, info):
    answer = bfs(n,info)
    
    if not answer:
        return[-1]
    else:
        return answer[-1]