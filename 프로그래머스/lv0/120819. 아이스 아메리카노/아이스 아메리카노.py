def solution(money):
    count = 0
    while money >= 5500:
        count += 1
        money -= 5500
    answer = []
    answer.extend([count,money])
    return answer