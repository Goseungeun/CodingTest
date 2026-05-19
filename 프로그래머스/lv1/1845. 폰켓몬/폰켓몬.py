def solution(nums):
    s_nums = list(set(nums))
    if len(s_nums) >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(s_nums)
    return answer