import re

list1 = []
list2 = []
simScore = 0
count = 0
L1count = 0
L2count = 0

with open("data.txt") as file:
    input = list(map(int, file.read().split()))

for i in input:
    
    if count % 2 == 0:
        list1.append(input[count])
    else:
        list2.append(input[count])
    count = count + 1
    
L1count = 0
for i in list1:
    appearences = 0
    L2count = 0
    x = list1[L1count]
    for j in list2:
        if x == list2[L2count]:
            appearences = appearences + 1
        L2count = L2count + 1
    simScore = simScore + (x * appearences)
    L1count = L1count + 1
print(simScore)
