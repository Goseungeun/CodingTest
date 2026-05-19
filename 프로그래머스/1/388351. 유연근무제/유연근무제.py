def cal_safetime(schedules):
    #출근 인정 시각 계산
    safetimes = []
    for schedule in schedules:
        h = schedule // 100
        m = schedule % 100
        m = m + 10
        if m >= 60:
            h += 1
            m -= 60
        safe_time = h *100 + m
        safetimes.append(safe_time)
    return safetimes

def is_late(safetime,timelog,startday):
    flag = True
    for time in timelog:
        if startday % 7 == 6 or startday % 7 == 0:
            startday += 1
            continue
        if time > safetime:
            flag = False
            break
        startday += 1
    return flag
        
def solution(schedules, timelogs, startday):
    safetimes = cal_safetime(schedules)
    answer = 0
    for i in range(len(safetimes)):
        if is_late(safetimes[i],timelogs[i],startday):
            answer += 1
    return answer