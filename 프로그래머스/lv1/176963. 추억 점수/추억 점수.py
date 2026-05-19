def solution(name, yearning, photo):
    point_dict = {name[i]:yearning[i] for i in range(len(name))}
    answer = []
    for ph in photo:
        sum_point = 0
        for nm in ph:
            try:
                sum_point += point_dict[nm]
            except:
                sum_point += 0
        answer.append(sum_point)
    
    return answer