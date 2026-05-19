def solution(picks, minerals):
    m_dict = {"diamond":0,"iron":0,"stone":0}
    length = min(5*sum(picks),len(minerals))
    damage = [[1,1,1],[5,1,1],[25,5,1]]
    l = []
    for i in range(length):
        m_dict[minerals[i]] += 1
        if (i + 1) % 5 == 0 or i == length -1:
            l.append([m_dict["diamond"],m_dict["iron"],m_dict["stone"]])
            m_dict = {"diamond":0,"iron":0,"stone":0}
    
    l.sort(key = lambda x:(x[0],x[1],x[2]),reverse = True)
    
    answer = 0
    print(l)
    
    for d,ir,s in l:
        for i in range(3):
            if picks[i] != 0:
                answer += ((damage[i][0] *d) +(damage[i][1] * ir)+(damage[i][2] * s))
                picks[i] -= 1
                break
    
    return answer