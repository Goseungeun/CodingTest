n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
costs = [[-1] * n for _ in range(n)]

costs[0][0] == 0
def count_cost(r,c):
    if r == 0 and c == 0:
        costs[r][c] = 0
    elif r == 0:
        if board[r][c-1] > board[r][c]:
            costs[r][c] = costs[r][c-1]
        else:
            costs[r][c] = costs[r][c-1] + (board[r][c] - board[r][c-1] + 1)
    elif c == 0:
        if board[r-1][c] > board[r][c]:
            costs[r][c] = costs[r-1][c]
        else:
            costs[r][c] = costs[r-1][c] + (board[r][c] - board[r-1][c] + 1)

    else:
        left_cost = costs[r][c-1]
        top_cost = costs[r-1][c]
        if board[r][c-1] <= board[r][c]:
            left_cost += board[r][c] - board[r][c-1] + 1
        if board[r-1][c] <= board[r][c]:
            top_cost += board[r][c] - board[r-1][c] + 1
        
        costs[r][c] = min(left_cost,top_cost)

for i in range(n):
    for j in range(n):
        count_cost(i,j)

print(costs[n-1][n-1])