#last value index
""" temp = [1,12,3,4,4,5,12,15,13,11]
temp.reverse()
index = len(temp) - temp.index(12) - 1
print(index) """

array = [4, 7, 9, 7, 2, 7]

# Find all indices of the value 7
indices = []
start = 0

while True:
    try:
          index = array.index(7, start)
          indices.append(index)
          start = index + 1
    except:
         break
    
""" #pedejais index
indices = []
start = 0
while True:
    try:
          index = array.index(1, start)
          indices.append(index)
          start = index + 1
    except:
         break

# o lites
indicesO = []
start = 0
while True:
    try:
          index = array.index(0, start)
          indicesO.append(index)
          start = index + 1
    except:
         break """
