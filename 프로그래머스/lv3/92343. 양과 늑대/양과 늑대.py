l = [-1] * 20 #왼쪽 노드
r = [-1] * 20 #오른쪽 노드
val = [] # 양/늑대 값
n = 0
ans = 0
vis = [0]*(1<<17) # vis[x] : 상태 x를 방문했는가?

#주어진 상태에서 모을 수 있는 양의 최댓값 찾는 함수
def count_max_sheep(state):
    global ans
    if vis[state]: return None  # 이미 방문한 상태이면 함수 종료
    vis[state] = 1 #현재 상태 방문으로 처리
    #wolf : 늑대의 수, num : 전체 노드의 수
    wolf, num = 0, 0
    for i in range(n):  #주어진 노드만큼 반복문을 돌면서
        if state & (1<<i):
            num += 1
            wolf += val[i]
    # 만약 늑대가 절반 이상일 경우 양을 최대로 얻을 수 없는 상태이니 종료
    if 2*(wolf) >= num: return None
    # 현재 state에서 얻은 양의 수가 ans 보다 큰 경우 ans를 갱신
    ans = max(ans, num - wolf)
    
    for i in range(n):
        if not state & (1<<i):  #현재 보고있는 i번째 노드가 현재 상태에 존재하지 않으면 넘어감
            continue
        #현재 보고 있는 i 노드에 자식이 존재하면, 해당 자식을 포함한 상태에서 최대로 모을 수 있는 양의 개수 세기
        if l[i] != -1:
            count_max_sheep(state|(1<<l[i]))
        if r[i] != -1:
            count_max_sheep(state|(1<<r[i]))
            
def solution(info, edges):
    global val,n
    n = len(info)
    val = info[:]
    for u,v in edges:
        if l[u] == -1:
            l[u] = v
        else:
            r[u] = v
    
    count_max_sheep(1)  #루트부터 시작
    return ans