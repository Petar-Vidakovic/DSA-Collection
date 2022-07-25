import numpy as np
import timeit

R = 4 # row
C = 7  # col
Y = 3  # fold
# R, C, Y = 316, 316, 157
lines = [[line.strip()] for line in open("input.txt")]
sample = [[0, 0, 1], [1, 0, 0]]
sample2 = [[0, 1, 0, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 1, 0, 1]]
card = np.array(sample2)
print(card)
print()

i = 0
# check that the fold point is in range
while Y-i-1 >= 0 and Y+1 < C:
    for j in range(R):
        # if they dont match assgin a 1
        if card[j][Y-i-1] != card[j][Y-i-1]:
            card[j][Y-i-1] = 1
    i += 1

for i in range(R):
    counter = C - 2 * Y
    l = C - 1
    while counter > 0:
        print(card[i][l], end=' ')
        l -= 1
        counter -= 1
    for j in range(Y):
        print(card[i][j], end=' ')
    print()


