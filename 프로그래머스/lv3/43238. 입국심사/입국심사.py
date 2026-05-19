def solution(n, times):
    max_time = min(times) * n
    start = 1
    end = max_time
    answer = 0
    while start <= end:
        mid = (start + end)//2
        max_people = 0
        for t in times:
            max_people += mid//t
        if max_people < n :
            start = mid +1
        elif max_people >= n :
            answer = mid
            end = mid -1

    return answer