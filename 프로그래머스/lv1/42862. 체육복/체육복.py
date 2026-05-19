def solution(n, lost, reserve):
    s_lost = set(lost)
    s_res = set(reserve)
    check = [0]*(n+2)
    inter = s_lost&s_res
    s_res = s_res - inter
    s_lost -= inter
    
    for l in s_lost:
        check[l] = -1
    
    for r in s_res:
        if check[r-1] == -1:
            check[r-1] += 1
        elif check[r+1] == -1:
            check[r+1] += 1
    
    c = check.count(-1)
    answer = n - c
    
        
    return answer