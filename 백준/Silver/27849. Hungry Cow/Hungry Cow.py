n,t = map(int,input().split())
give_farmer = [list(map(int,input().split())) for _ in range(n)]

give_farmer.append([t+1,0])
total_h = 0

eat_h = 0

for i in range(n):
    total_h += give_farmer[i][1]
    if give_farmer[i+1][0] - give_farmer[i][0] < total_h:
        eat_h += give_farmer[i+1][0] - give_farmer[i][0]
        total_h -= give_farmer[i+1][0] - give_farmer[i][0]
    else:
        eat_h += total_h
        total_h = 0

print(eat_h)