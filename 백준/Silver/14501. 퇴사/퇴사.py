# 퇴사
n = int(input())   #일하는 총 날짜
tList = []  #상담 완료하는데 걸리는 시간
pList = []  #상담 수익 list
dp = [] #해당 날짜까지의 최대 수익 저장 list

for _ in range(n):  #n번 반복하면서 상담 소요 시간과 수익 저장
    a, b = map(int,input().split())

    tList.append(a)
    pList.append(b)
    dp.append(b)
dp.append(0)    #비교를 위한 dp 하나 더 추가
    
for i in range(n-1,-1,-1):  #뒤에서부터 확인
    if tList[i] + i > n:    #상담 소요기간이 퇴사 날짜를 넘어가면
        dp[i] = dp[i+1]     #상담 X => 이 상담에 대한 수익 없음
    else :  #상담 날짜가 퇴사 날짜를 넘어가지 않는다면
        dp[i] = max(dp[i+1], pList[i]+dp[i+tList[i]])   
        #상담을 안할 때의 수익과 상담 진행 후, 상담 종료후의 수익과 비교해서 최댓값 선택

print(dp[0])    #제일 처음 값이 최댓값