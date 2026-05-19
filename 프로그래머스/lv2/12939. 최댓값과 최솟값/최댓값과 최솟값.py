def solution(s):
    
    ss = list(map(int, s.split(" ")))
    answer = f'{min(ss)} {max(ss)}'
    return answer