def solution(players, m, k):
    answer = 0
    server = [0 for _ in range(24)]
    
    for i in range(24):
        need = players[i] // m
        if need > server[i]:
            add = need - server[i]
            answer += add
            
            for j in range(i,min(i+k,24)):
                server[j] += add
                
            
    return answer