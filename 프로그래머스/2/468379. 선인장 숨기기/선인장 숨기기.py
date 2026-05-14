from collections import deque

def solution(m, n, h, w, drops):
    INF = 10**9
    dmap = [[INF] * n for _ in range(m)]

    for t, (r, c) in enumerate(drops, start=1):
        dmap[r][c] = t

    row_min = [[0] * (n - w + 1) for _ in range(m)]

    for i in range(m):
        dq = deque()

        for j in range(n):
            while dq and dmap[i][dq[-1]] >= dmap[i][j]:
                dq.pop()

            dq.append(j)

            if dq[0] <= j - w:
                dq.popleft()

            if j >= w - 1:
                row_min[i][j - w + 1] = dmap[i][dq[0]]

    rect_min = [[0] * (n - w + 1) for _ in range(m - h + 1)]

    for j in range(n - w + 1):
        dq = deque()

        for i in range(m):
            while dq and row_min[dq[-1]][j] >= row_min[i][j]:
                dq.pop()

            dq.append(i)

            if dq[0] <= i - h:
                dq.popleft()

            if i >= h - 1:
                top = i - h + 1
                rect_min[top][j] = row_min[dq[0]][j]

    latest = -1
    ans = [0, 0]

    for i in range(m - h + 1):
        for j in range(n - w + 1):
            if rect_min[i][j] > latest:
                latest = rect_min[i][j]
                ans = [i, j]

    return ans