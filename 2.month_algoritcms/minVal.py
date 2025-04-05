#bublle sorting
array = [64, 34, 25, 5, 22,22, 11, 11, 90, 12]

for x in range(len(array)):
    for i in range(len(array)):
        if array[x]<array[i]:
            array[x], array[i]= array[i], array[x]
print(array)
