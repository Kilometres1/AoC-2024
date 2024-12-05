import re

list1 = []
list2 = []
output = 0
count = 0

with open("data.txt") as file:
    input = list(map(int, file.read().split()))

for i in input:
    
    if count % 2 == 0:
        list1.append(input[count])
    else:
        list2.append(input[count])
    count = count + 1

list1.sort()
list2.sort()

count = 0
for i in list1:
    output = output + (abs(list1[count] - list2[count]))
    count = count + 1


print(output)

