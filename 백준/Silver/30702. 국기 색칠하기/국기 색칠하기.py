from collections import deque

n,m = map(int,input().split())
flag_a = [list(input()) for _ in range(n)]
flag_b = [list(input()) for _ in range(n)]
vis_a = [[0]*m for _ in range(n)]
new_a = [[' '] *m for _ in range(n)]

dir = [(-1,0),(0,1),(1,0),(-1,0)]
for i in range(n):
    for j in range(m):
        if vis_a[i][j] == 0:
            color = flag_b[i][j]
            q = deque()
            q.append([i,j])
            vis_a[i][j] = 1
            new_a[i][j] = color

            while q:
                c_i,c_j = q.popleft()
                for d in range(4):
                    n_i,n_j = c_i + dir[d][0], c_j + dir[d][1]
                    if 0 <= n_i < n and 0 <= n_j < m:
                        if vis_a[n_i][n_j] == 0 and flag_a[c_i][c_j] == flag_a[n_i][n_j]:
                            new_a[n_i][n_j] = color
                            vis_a[n_i][n_j] = 1
                            q.append([n_i,n_j])

if new_a == flag_b:
    print("YES")
else:
    print("NO")