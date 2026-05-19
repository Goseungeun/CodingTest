def solution(today, terms, privacies):
    terms_dic = {}
    t_y, t_m, t_d = map(int,today.split('.'))
    answer = []
    
    for i in range(len(terms)):
        terms_dic[terms[i].split()[0]] = terms[i].split()[1]
    for j in range(len(privacies)):
        in_date, term = privacies[j].split()
        in_y,in_m,in_d = map(int,in_date.split('.'))
        in_m += int(terms_dic[term])
        in_d -= 1
        if in_d == 0:
            in_m -= 1
            in_d = 28
        while (in_m > 12):
            in_y += 1
            in_m -= 12
        
        if t_y > in_y:
            answer.append(j+1)
            continue
        elif t_y == in_y and t_m > in_m:
            answer.append(j+1)
            continue
        elif t_y == in_y and t_m == in_m and t_d > in_d:
            answer.append(j+1)
            
    return answer