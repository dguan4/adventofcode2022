###  parse from input.txt file and return as list
def getFromInput():
    currMax = 0
    with open('input.txt', 'r') as file:
        localMax = 0
        for line in file:
            if line == '\n':
                currMax = max(currMax, localMax)
                localMax = 0
                print('true')
            else:
                localMax += int(line)

    return currMax
                

lines = getFromInput()
print(lines)
