f = open('naj.txt','w')
f.write("whoops! ")
f.close()

f = open('naj.txt','r')
print(f.read())