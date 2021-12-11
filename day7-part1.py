import statistics

input = []
with open('data/inputDay7.txt', 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        line = line.split(",")
        for x in line:
            input.append(int(x))

print("Initial state:", input)

totalFuelUsed = 0
targetPosition = int(statistics.median(input))

for i in range(len(input)):
    totalFuelUsed += abs(targetPosition - input[i])

print(totalFuelUsed)
