r = []

def f(result, numbers, i):
    
    # numbers 다 돌았을 때, 탈출!
    if len(numbers) == i :
        r.append(result)
        return 0
    
    f(result+numbers[i], numbers, i+1)
    f(result-numbers[i], numbers, i+1)
    
    
    

def solution(numbers, target):
    
    f(0,numbers,0)
    
    
    answer = r.count(target)
    return answer