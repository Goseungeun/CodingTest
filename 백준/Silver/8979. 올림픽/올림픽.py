n,k = map(int,input().split())
countries = [list(map(int,input().split())) for _ in range(n)]

countries.sort(key=lambda x: (x[1],x[2],x[3]),reverse= True)
#print(countries)
rank = 1
prev_g,prev_s,prev_b = countries[0][1],countries[0][2],countries[0][3]
i = 0

while countries[i][0] != k:
    if prev_g != countries[i][1] or prev_s != countries[i][2] or prev_b != countries[i][3]:
        #print("here")
        rank = i+1
    prev_g,prev_s,prev_b = countries[i][1],countries[i][2],countries[i][3]
    
    i += 1

if prev_g != countries[i][1] or prev_s != countries[i][2] or prev_b != countries[i][3]:
    rank += 1

print(rank)