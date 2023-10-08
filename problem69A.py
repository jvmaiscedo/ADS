n = int(input())
x= []
y=[]
z=[]

for i in range(n):
    vetor = input().split(" ")
    x.append(int(vetor[0]))
    y.append(int(vetor[1]))
    z.append(int(vetor[2]))

if sum(x)==0 and sum(y)==0 and sum(z)==0:
    print("YES")
else:
    print("NO")
