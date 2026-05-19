def solution(s):
    prev = ' '
    answer = ''
    for i in s:
        if prev ==' ':
            answer += i.upper()
        else:
            answer += i.lower()
        prev = i
    return answer