n=int(input())
l=[]
for i in range(n):
    part=input().split()
    initial="".join(word[0]+"." for word in part[:-1])
    last=part[-1]
    k=initial+last
    l.append(k)
l.sort()
for i in l:
    print(i)



