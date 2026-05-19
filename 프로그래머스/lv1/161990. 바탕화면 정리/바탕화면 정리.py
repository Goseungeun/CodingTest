def solution(wallpaper):
    row_list = []
    col_list = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                row_list.append(i)
                col_list.append(j)
                
            
    answer = [min(row_list), min(col_list), max(row_list)+1,max(col_list)+1]
    return answer