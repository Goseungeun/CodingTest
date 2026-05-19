def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        real = bin(arr1[i] | arr2[i])[2:].zfill(n)
        real_map = real.replace('1','#').replace('0',' ')
        answer.append(real_map)
        
    return answer