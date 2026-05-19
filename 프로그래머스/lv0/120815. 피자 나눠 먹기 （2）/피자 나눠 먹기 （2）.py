import math
def solution(n):
    gg = math.gcd(6,n)
    n_pizza =  gg * (n//gg) * (6//gg)
    answer = n_pizza // 6
    return answer