def solution(array, commands):
    answer = []
    for c in commands:
        S=array[c[0]-1:c[1]]
        S.sort()
        answer.append(S[c[2]-1])
    
    return answer