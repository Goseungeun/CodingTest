n,k = map(int,input().split())
countries = [list(map(int,input().split())) for _ in range(n)]

countries.sort(key=lambda x: (x[1],x[2],x[3]),reverse= True)
#print(countries)
idx = [countries[i][0] for i in range(n)].index(k)
for i in range(n):
    if countries[idx][1:] == countries[i][1:]:
        print(i+1)
        break