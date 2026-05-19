def solution(p):
    if len(p) == 0:
        return ''
    count = 0
    flag = True
    
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0 :
            break
        if count < 0:
            flag = False
    u,v = p[:i+1],p[i+1:]
    if flag:
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + ''.join(['(' if x == ')' else ')' for x in u[1:i]])
     
    