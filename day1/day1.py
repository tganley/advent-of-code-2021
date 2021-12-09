import numpy as np

count = 0
f = open("day1/day1_data.txt","r")
lines = list(map(int,f.readlines()))
print(np.size(lines))
for i in range(np.size(lines)-3):
    if lines[i] < lines[i+3]:
        count += 1

print(count)
f.close()
