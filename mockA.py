N=int(input())
brides=input()
b=list(brides)
grooms=input()
g=list(grooms)
count=0
for bride in range (len(b)):
  for groom in range (len(g)):
    if(b[0]==g[0]):
      b.pop(0)
      g.pop(0)
      count+=1
    else:
      x=g.pop(0)
      g.append(x)
ans=N-count
print(ans)
