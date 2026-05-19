from collections import deque

def solution(queue1, queue2):
    s_q1 = sum(queue1)
    mid_sum = (s_q1 + sum(queue2))//2
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = 0
    
    for answer in range((len(queue1) + len(queue2)) * 2 + 1):
        if s_q1 > mid_sum:
            x = q1.popleft()
            s_q1 -= x
            q2.append(x)
        elif s_q1 < mid_sum:
            x = q2.popleft()
            s_q1 += x
            q1.append(x)
        elif s_q1 == mid_sum:
            break

    if answer == (len(queue1) + len(queue2)) * 2 :
        answer = -1
        
    return answer