from sys import setrecursionlimit
setrecursionlimit(10000)

def solution(nodeinfo):
    nodeinfo = sorted([(x,y,i+1) for i,(x,y) in enumerate(nodeinfo)],
                     key = lambda x:x[0])
    answer = [[],[]]
    
    def Root(nodeinfo):
        if nodeinfo:
            high = (0,-1,0) #index, y, nodenum
            for i,(x,y,nodenum) in enumerate(nodeinfo):
                if high[1] < y:
                    high = (i,y,nodenum)
            answer[0].append(high[2])
            left,right = nodeinfo[:high[0]], nodeinfo[high[0]+1:]
            Root(left), Root(right)
            answer[1].append(high[2])
    Root(nodeinfo)
            
    return answer