dx = [0,0,1,-1]
dy = [1,-1,0,0]
direction_dic = {'E':0,'W':1,'S':2,'N':3}

def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                cr_position = [i,j]
    
    for route in routes:
        d,l = route.split(" ")
        d_code = direction_dic[d]
        move(d_code,int(l),park,cr_position)
        #print(cr_position)
    return cr_position

def move(d,l,park,current):
    flag = 1
    
    #임시 x,y
    t_x = current[0]
    t_y = current[1]
    
    for _ in range(l):
        nx = t_x + dx[d]
        ny = t_y + dy[d]
        if 0 <= nx < len(park) and 0 <= ny < len(park[0]):
            if park[nx][ny] == 'X':
                flag = 0
                break
            else:
                t_x = nx
                t_y = ny
        else:
            flag = 0
            break
    if flag:
        current[0] = t_x
        current[1] = t_y
