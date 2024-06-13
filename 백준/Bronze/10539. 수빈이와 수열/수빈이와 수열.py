n = int(input())
b_list = list(map(int,input().split()))
a_list = []
a_list.append(b_list[0])

for i in range(1,n):
    s = b_list[i] * (i+1)
    t = s - sum(a_list)
    a_list.append(t)

print(' '.join(map(str,a_list)))