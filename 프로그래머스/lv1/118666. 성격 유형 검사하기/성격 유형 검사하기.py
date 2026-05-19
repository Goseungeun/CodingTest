def solution(survey, choices):
    score_dic = {"R" : 0 ,"T" : 0 ,"C" : 0 ,"F" : 0 ,"J" : 0 ,"M" : 0 ,"A" : 0 ,"N" : 0 }
    
    for i,s in enumerate(survey):
        if choices[i] < 4:
            score_dic[s[0]] += abs(choices[i] - 4)
        elif choices[i]>4:
            score_dic[s[1]] += abs(choices[i] - 4)
    answer = ''  
    
    if score_dic["R"] < score_dic["T"]:
        answer += 'T'
    else:
        answer += 'R'
        
    if score_dic["C"] < score_dic["F"]:
        answer += 'F'
    else:
        answer += 'C'
        
    if score_dic["J"] < score_dic["M"]:
        answer += 'M'
    else:
        answer += 'J'

    if score_dic["A"] < score_dic["N"]:
        answer += 'N'
    else:
        answer += 'A'
    
    return answer