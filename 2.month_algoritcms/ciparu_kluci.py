v = int(input())
c = 0
array = []
while c < v:
    k = int(input())
    array.append(k)
    c+=1
#array = [2, 7, 2, 1, 3]
#[2,0,1,3,1] [9, 1, 6, 8, 0, 8, 3, 7, 1, 5, 0, 7, 7]
indices = []
start = 0
while True:
    try:
          index = array.index(1, start)
          indices.append(index)
          start = index + 1
    except:
         break
#skaitlīšu kartošana
jaunsCip=array[0]
cip = []
s=-1
for x in array:
    s+=1
    if s == indices[-1] and cip[0] == 0:
        cip.insert(0, x)
        continue
    elif x == 0 and s > indices[-1]:
        cip.append(x)
        continue
    if x > jaunsCip:
        cip.append(x)
    else:
        cip.insert(0, x)
        jaunsCip = cip[0] 
        
rez = ''.join([str(h) for h in cip]) 
print(rez)
