import numpy as np

f = open("day3/day3_data.txt","r")
entries = f.readlines()
line_count = np.size(entries)
bit_count = len(entries[0]) - 1

entries_int = []
gamma = 0
epsilon = 0

for i  in range(line_count):
    entries_int.append(int(entries[i], 2))

for j in range(bit_count):
    counter = 0
    for i in range(line_count):
        if ((entries_int[i] >> j) & 0x1) == 1:
            counter += 1
        else:
            counter -= 1
    if counter > 0:
        gamma |= (1 << j)
    else:
        epsilon |= (1 << j)

print("Gamma:", gamma, "Epsilon:", epsilon)
print("Gamma * Epsilon:", gamma * epsilon)
