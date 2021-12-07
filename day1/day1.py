import numpy as np

count = 0
f = open("day1_data.txt","rb")
lines = list(map(int,f.readlines()))
print(np.size(lines))
for i in range(np.size(lines)-1):
    if lines[i] < lines[i+1]:
        #print(lines[i] + "<" + lines[i+1])
        count += 1

print(count)
f.close()
