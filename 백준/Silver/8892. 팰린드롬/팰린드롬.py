def pelin():
    k = int(input())
    str_list = []
    for _ in range(k):
        str_list.append(input())
    for i in range(len(str_list)):
        for j in range(len(str_list)):
            if i != j:
                word = str_list[i] + str_list[j]
                if word == word[::-1]:
                    return word
    return 0

t = int(input())
for _ in range(t):
    ans = pelin()
    print(ans)
                    
