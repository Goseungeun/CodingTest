import sys
input = sys.stdin.readline
n,m = map(int,input().split())
s = list(map(int,input().split()))
count = 0
e = 0

for i in range(n): #초기 count를 구해주는 동작 안해주면 0만 가득한 리스트를 제외하고는 틀림. ex반례
    if s[i] == 0:
        e = 0
    elif s[i] == 1:
        if e ==0:
            count+=1
            e = 1
            
for i in range(m):
    a = list(map(int,input().split()))
    if a[0] == 1 and s[a[1]-1] == 0:
        a[1]-=1
        if a[1] == 0:
            if s[1] ==0:
                count+=1
                s[a[1]] = 1
                
        elif a[1] == n-1:
            if s[n-2] ==0:
                count+=1
                s[a[1]] = 1
        else:
            if (s[a[1]-1] == 1 and s[a[1]+1] == 1): #1번
                count-=1
                s[a[1]] = 1
                    
            elif (s[a[1]-1] == 0 and s[a[1]+1] == 0): #2번
                s[a[1]] = 1
                count+=1
            else: #3번
                s[a[1]]=1
    
    elif a[0]==0:
        print(count)