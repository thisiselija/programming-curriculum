koloSk = 3
rindSk = 3
i = 1
c = 1
while i <= rindSk:
    k = 1
    if i%2 ==0:
        koloSk+=1
    else:
        koloSk = 3
    while k <= koloSk:
        print(c, end='')
        c+=1
        k+=1 
    print('\n')
    i+=1