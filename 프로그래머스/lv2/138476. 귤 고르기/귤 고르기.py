from collections import Counter
def solution(k, tangerine):
    num_tanger = sorted(Counter(tangerine).items(),key=lambda x: x[1],reverse=True)
    answer = 0
    for _,i in num_tanger:
        answer += 1
        k -= i
        if k <= 0 :
            break
    return answer