# def solution(friends, gifts):
#     gift_matrix = [[0 for j in range(len(friends))] for i in range(len(friends))]
#     dic_name = {}
#     g_r_index = [0]* len(friends)
#     next_month = [0]* len(friends)
#     for i,f in enumerate(friends):
#         dic_name[f] = i
        
#     for gift in gifts:
#         giver, reciever = gift.split()
#         g_i, r_i = dic_name[giver],dic_name[reciever]
#         gift_matrix[g_i][r_i] += 1
#         g_r_index[g_i] += 1
#         g_r_index[r_i] -= 1
    
#     for i in range(len(friends)):
#         for j in range(i):
#             if gift_matrix[i][j] > gift_matrix[j][i]:
#                 next_month[i] += 1
#             elif gift_matrix[j][i] > gift_matrix[i][j]:
#                 next_month[j] += 1
#             else:
#                 if g_r_index[i] > g_r_index[j]:
#                     next_month[i] += 1
#                 elif g_r_index[i] < g_r_index[j]:
#                     next_month[j] += 1
#     return max(next_month)

def solution(friends, gifts):
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends)
    p = [0] * l
    answer = [0] * l
    gr = [[0] * l for i in range(l)]
    for i in gifts:
        a, b = i.split()
        gr[f[a]][f[b]] += 1
    for i in range(l):
        print([k[i] for k in gr])
        p[i] = sum(gr[i]) - sum([k[i] for k in gr])
        
    
    for i in range(l):
        for j in range(l):
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            elif gr[i][j] == gr[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
    return max(answer)