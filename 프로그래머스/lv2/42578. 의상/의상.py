def solution(clothes):
    answer = 0
    cloth_dict = {}
    
    for cloth in clothes:
        if cloth[1] in cloth_dict:
            cloth_dict[cloth[1]] += 1
        else:
            cloth_dict[cloth[1]] = 1
    
    answer = 1
    
    for v in cloth_dict.values():
        answer *= (v+1)
    
    answer -= 1
    
    return answer