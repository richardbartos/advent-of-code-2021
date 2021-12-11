import numpy as np

input = []
maxDimensions = [0, 0]

with open('data/inputDay5-sample.txt', 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        line = line.split(" -> ")
        for i in range(len(line)):
            line[i] = line[i].split(",")
            for ii in range(len(line[i])):
                line[i][ii] = int(line[i][ii])
                if ii == 0:
                    if line[i][ii] > maxDimensions[0]:
                        maxDimensions[0] = line[i][ii]
                else:
                    if line[i][ii] > maxDimensions[1]:
                        maxDimensions[1] = line[i][ii]

        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            input.append(line)

print (input)

mapArray = np.zeros((maxDimensions[0], maxDimensions[1]), dtype=int)

for i in range(len(input)):
    print ("Mrdat na to.")

print (mapArray)
