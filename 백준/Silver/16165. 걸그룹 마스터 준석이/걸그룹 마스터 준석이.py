n,m = map(int,input().split())
groups = {}
member = {}
for _ in range(n):
    gr_name = input()
    mem_num = int(input())
    members = []
    for _ in range(mem_num):
        name = input()
        member[name] = gr_name
        members.append(name)
    groups[gr_name] = sorted(members)

for _ in range(m):
    com = input()
    ty = int(input())
    if ty == 0:
        for i in groups[com]:
            print(i)
    elif ty == 1:
        print(member[com])