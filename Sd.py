import math
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]

def mean (d):
    n = len(d)
    total = 0
    for i in d:
        total+=int(i)
    m=total/n
    return m

mn = mean(data)
sqlist = []

for element in data:
    minus = int(element) - mn
    sq = minus**2
    sqlist.append(sq)

sum = 0
for i in sqlist:
    sum += i

result = sum/(len(data)-1)

sd = math.sqrt(result)
print(sd)