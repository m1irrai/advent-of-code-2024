numList = []
numList1 = []
numList2 = []
with open("input.txt", 'r') as f:
    for line in f.readlines():
        line = line.replace("\n", "")        
        numList.append(line.split('   '))
for line in numList:
    numList1.append(line[0])
    numList2.append(line[1])
    
numList1.sort()
numList2.sort()

total = 0
for o in range(len(numList2)):
    total += abs(int(numList1[o]) - int(numList2[o]))

total2 = 0
for y in range(len(numList1)):
    n = numList2.count(numList1[y])
    total2 += n * int(numList1[y])
print(total2)
