import regex as re

file = open("day4.txt", "r")
num_games = file.readlines()  # Number of lines in file as number of games
file.seek(0)  # Return to beginning of file
multiplier_list = []
resultList = [1] * len(num_games)


def part_one():
    total = 0  # Total points from all scratchcards
    while True:
        line = file.readline()
        if not line:
            break
        winning = re.findall(r':\s(.*)\s\|', line)
        winning = [r.split() for r in winning]  # Winning numbers as list
        numbers = re.findall(r'\|\s(.*)', line)
        numbers = [r.split() for r in numbers]  # Scratched numbers as list

        c = sum(el in winning[0] for el in numbers[0])  # Number of scratched numbers that are winning

        if c == 0 or c == 1:  # If 0 or 1 hit, add hit to total
            total += c

        else:  # Doubles the number for every hit if larger than 1
            total += 2 ** (c - 1)

    print(total)


def part_two():
    for line in num_games:
        winning = line.split(": ")[1].split("| ")
        winning_numbers = re.findall(r"\d+", winning[0])  # Winning numbers as list
        scratch_numbers = re.findall(r"\d+", winning[1])
        winning_numbers = list(map(int, winning_numbers))  # Convert both lists to integers
        scratch_numbers = list(map(int, scratch_numbers))

        temp_multiplier = 0  # Number of wins for current game
        for n in scratch_numbers:
            if n in winning_numbers:
                temp_multiplier += 1

        multiplier_list.append(temp_multiplier)  # List with the wins for every game

    for j in range(len(multiplier_list)):
        for i in range(multiplier_list[j]):
            resultList[i + j + 1] += resultList[j]

    print(sum(resultList))


part_one()
part_two()
