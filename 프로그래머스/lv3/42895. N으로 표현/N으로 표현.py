def cal_op(X,Y):
    n_set = set()
    for x in X:
        for y in Y:
            n_set.add(x+y)
            n_set.add(x-y)
            n_set.add(x*y)
            if y != 0 :
                n_set.add(x//y)
    return n_set

def solution(N, number):
    answer = -1
    if number == N:
        return 1
    dp = {}
    dp[1] = {N}
    
    for n in range(2,9):
        temp_set = {int(str(N)*n)}
        i = 1
        while i < n:
            temp_set.update(cal_op(dp[i],dp[n-i]))
            i+=1
        if number in temp_set:
            answer = n
            break
        dp[n] = temp_set
    
    return answer