n = int(input())

for _ in range(n):
    a,b,c = list(map(int,input().split()))
    if a+b+c == 180:
        ans = "Seems OK"
    else:
        ans = "Check"
    
    print(a,b,c,ans)