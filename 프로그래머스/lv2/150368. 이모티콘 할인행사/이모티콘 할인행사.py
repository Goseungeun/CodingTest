from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    sale = list(product([10,20,30,40], repeat = len(emoticons)))
    
    for s in sale :
        total_sub = 0
        total_value = 0
        
        for u in users :
            value = 0
            for i, e in enumerate(emoticons):
                if s[i] < u[0]:
                    continue
                value += e - e*s[i]/100
            if u[1] <= value:
                total_sub += 1
            else :
                total_value += value
                
        if answer[0] <= total_sub :
            if answer[0] == total_sub and answer[1] < total_value:
                answer = [total_sub, total_value]
            elif answer[0] < total_sub:
                answer = [total_sub, total_value]
    
    return answer