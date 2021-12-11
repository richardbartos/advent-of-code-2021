input = []
with open('inputDay6.txt', 'r') as fh:
    for line in fh.readlines():
        line = line.strip() 
        line = line.split(",")
        for x in line:
            input.append(int(x))

print("Initial state:",input)

def runLanternfishOrgy(numberOfDays):
    day = 1
    while day <= numberOfDays:
        for i in range(len(input)):
            if input[i] == 0:
                input.append(8)
                input[i] = 6
            else:
                input[i] -= 1
        day += 1
    print("Total number of fish:",len(input))
        

runLanternfishOrgy(256)