import regex as re

file = open("day4.txt", "r")
numGames = file.readlines()
multiplierList = []
resultList = [1] * len(numGames)

for line in numGames:
    winning = line.split(": ")[1].split("| ")
    winningNumbers = re.findall("\d+", winning[0])
    scratchNumbers = re.findall("\d+", winning[1])
    winningNumbers = list(map(int, winningNumbers))
    scratchNumbers = list(map(int, scratchNumbers))

    tempMultiplier = 0
    for n in scratchNumbers:
        if n in winningNumbers:
            tempMultiplier += 1

    multiplierList.append(tempMultiplier)

for j in range(len(multiplierList)):
    for i in range(multiplierList[j]):
        resultList[i+j+1] += resultList[j]

print(sum(resultList))
