def cadbury(P, Q, R, S):
    count=0
    for l in range(P,Q+1):
        for b in range(R,S+1):
            count=count+call(l,b)
    return count

def call(l,b):
    count=0
    dif=1
    while(dif):
        big=max(l,b)
        small=min(l,b)
        count=count+1
        dif=big-small
        if dif==0:
            return count
        else:
            l=min(l,b)
            b=dif
            
P=int(input())
Q=int(input())
R=int(input())
S=int(input())
ans=cadbury(P,Q,R,S)
print(ans)
