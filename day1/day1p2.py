###  parse from input.txt file and return as list
def getFromInput():
    sums = []
    with open('input.txt', 'r') as file:
        localMax = 0
        for line in file:
            if line == '\n':
                sums.append(localMax)
                localMax = 0
                print('true')
            else:
                localMax += int(line)

    return sorted(sums)
                

lines = getFromInput()
print(sum(lines[-3:]))
