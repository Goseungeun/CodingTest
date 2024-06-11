t = int(input())
for _ in range(t):
    n = int(input())
    left_box = list(map(int,input().split()))
    right_box = list(map(int,input().split()))

    car = 0
    cnt = 0
    for i in range(n):
        if left_box[i] + 1000 in right_box:
            cnt += 1
        if cnt == 2:
            cnt = 0
            car += 1
    
    print(car)