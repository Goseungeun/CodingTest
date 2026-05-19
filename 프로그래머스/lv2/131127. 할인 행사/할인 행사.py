from collections import Counter

def solution(want, number, discount):
    wantnum_dic = {}
    answer = 0
    for i in range(len(want)):
        wantnum_dic[want[i]] = number[i]
    for i in range(len(discount) - 9):
        c_discount = Counter(discount[i:i+10])
        if wantnum_dic == c_discount:
            answer += 1
    return answer