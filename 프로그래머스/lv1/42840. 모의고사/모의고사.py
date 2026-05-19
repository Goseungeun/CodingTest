def solution(answers):
    S=[0]*(4)
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    
    
    for i in range(len(answers)):
        if answers[i] ==one[i%5]:
            S[1]+=1
        if answers[i] ==two[i%8]:
            S[2]+=1
        if answers[i] ==three[i%10]:
            S[3]+=1

    answer=[i for i, ele in enumerate(S) if ele == max(S)]
    
    return answer