def solution(edges):
    max_node = max(map(max,edges))
    in_list = [0] * max_node
    out_list = [0] * max_node
    add_node = 0
    whole_graph = 0
    stick = 0
    eight = 0
    
    for edge in edges:
        out_list[edge[0]-1] += 1
        in_list[edge[1]-1] += 1
    
    for i,o in enumerate(out_list):
        if o == 0 and in_list[i] >= 1:
            stick += 1
        elif o >= 2:
            if in_list[i] == 0:
                add_node = i+1
                whole_graph = o
            else:
                eight += 1
    answer = [add_node,whole_graph - stick-eight,stick,eight]
    return answer