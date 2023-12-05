import regex as re
from functools import reduce
from operator import mul

def part_one():
    file = open("day2.txt", "r")
    counter = 0
    game_id = 1

    while True:
        line = file.readline()
        if not line:
            break
        line = line.split(":")[1]
        numbers_r = re.findall(r"([1][3-9]|[2][0-9])\sr", line)
        numbers_g = re.findall(r"([1][4-9]|[2][0-9])\sg", line)
        numbers_b = re.findall(r"([1][5-9]|[2][0-9])\sb", line)

        if numbers_r == [] and numbers_g == [] and numbers_b == []:  # If all games were valid, add game_id to counter
            counter += game_id
        game_id += 1
    file.close()
    print(counter)


def part_two():
    file = open("day2.txt", "r")
    temp_product = []
    while True:
        line = file.readline()
        if not line:
            break
        line = line.split(":")[1]  # Remove everything before :
        # Three lists, by color for the cubes
        numbers = [re.findall(r"(\d+)\sr", line), re.findall(r"(\d+)\sg", line), re.findall(r"(\d+)\sb", line)]
        # Converts str values to int in the lists
        numbers = list(map(lambda x: list(map(int, x)), numbers))
        # Saves the largest of each color to list
        largest_nums = list(map(max, numbers))
        # Product of the largest numbers added to list
        temp_product.append(reduce(mul, largest_nums, 1))
        """
        numbers_r = re.findall(r"(\d+)\sr", line)
        numbers_g = re.findall(r"(\d+)\sg", line)
        numbers_b = re.findall(r"(\d+)\sb", line)
        
        numbers_r = list(map(int, numbers_r))
        numbers_g = list(map(int, numbers_g))
        numbers_b = list(map(int, numbers_b))
        
        largest_r = 0
        largest_g = 0
        largest_b = 0
        
        for n in numbers_r:
            if n > largest_r:
                largest_r = n
        for n in numbers_g:
            if n > largest_g:
                largest_g = n
        for n in numbers_b:
            if n > largest_b:
                largest_b = n
        temp_product.append(largest_r * largest_b * largest_g)
        """
    file.close()
    print(sum(temp_product))

part_one()
part_two()
