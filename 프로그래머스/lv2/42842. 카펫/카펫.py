def solution(brown, yellow):
    plus = int(brown/2) - 2
    for a in range(1, plus):
        if yellow == a*(plus-a):
            return [plus-a+2,a+2]