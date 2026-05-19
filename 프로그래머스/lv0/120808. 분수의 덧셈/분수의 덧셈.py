import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    denom = denom1*denom2
    numer = numer1*denom2 + numer2*denom1
    
    gcd = math.gcd(numer,denom)
    if gcd != 1:
        numer//=gcd
        denom//=gcd
    
    answer.extend([numer,denom])
    return answer