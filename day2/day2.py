import numpy as np
horiz = 0
depth = 0
aim = 0

f = open("day2_data.txt","r")
actions = f.readlines()

for i in range(np.size(actions)):
    actions[i] = actions[i].split()

    if(actions[i][0] == "forward"):
        horiz += int(actions[i][1])
        depth += aim * int(actions[i][1])
    elif(actions[i][0] == "down"):
        aim += int(actions[i][1])
    elif(actions[i][0] == "up"):
        aim -= int(actions[i][1])

print("Depth: ", depth)
print("Horizontal: ", horiz)
print("Depth * Horizontal: ", depth*horiz)

f.close()
