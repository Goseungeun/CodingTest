def solution(n, m, section):
    painted, answer = section[0]-1,0
    for s in section:
        if painted < s:
            painted = s + m - 1
            answer += 1
    return answer