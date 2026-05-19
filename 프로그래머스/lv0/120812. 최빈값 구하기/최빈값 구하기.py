from collections import Counter

def solution(array):
    count = Counter(array).most_common()
    if len(count) > 1 :
        if count[0][1] == count[1][1]:
            answer = -1
            return answer
    answer = count[0][0]
    return answer