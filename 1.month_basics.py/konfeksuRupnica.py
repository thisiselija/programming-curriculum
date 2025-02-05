n = int(input('Ievadi konfekšu veidu skaitu: '))
m = int(input("Ievadi kastītei nepieciešamo sk: "))
l = []
i = 0
while i<n:
    veidi = input("ievadiet katra veida daudzumu: ")
    i+=1
    l.append(veidi)

for char in range(len(l)):
    l[char] = int(l[char])
#print(l)  

#kastīšu iepakojumi
v = []
for dal in l:
    aprekins= dal//m
    v.append(aprekins)   
print(min(v), end='' +' ')

#pārpalikums
p=[]
for parL in l:
    for parV in v:
        parpalikums = parL - 1*m
        
    p.append(parpalikums)
    print(p)
print(sum(p))