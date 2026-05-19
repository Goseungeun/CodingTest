def solution(arr):
    answer = []
    x=arr.pop()
    answer.append(x)
    
    for _ in range(len(arr)):
        y=arr.pop()
        if x!=y:
            answer.append(y)
            x=y
        else:
            continue
    answer.reverse()
    return answer