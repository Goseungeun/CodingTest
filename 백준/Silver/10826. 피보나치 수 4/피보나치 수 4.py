d = [0]*10001
d[0] = 0
d[1] = 1

for i in range(2,10001):
    d[i] = d[i-1]+d[i-2]

n = int(input())
print(d[n])