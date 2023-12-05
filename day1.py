import regex as re

def part_one():
    file = open("day1.txt", "r")
    result = []
    while True:
        line = file.readline()
        if not line:
            break
        numbers = re.findall(r'\d', line)
        numbers = list(map(int, numbers))
        first = numbers[0]
        last = numbers[-1]
        result.append(int(str(first) + str(last)))
    file.close()
    print(sum(result))

def part_two():
    file = open("day1.txt", "r")
    result = []
    number_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while True:
        line = file.readline()
        if not line:
            break
        numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        for i in range(len(numbers)):
            if numbers[i] in number_list:
                numbers[i] = number_list.index(numbers[i])
        numbers = list(map(int, numbers))
        first = numbers[0]
        last = numbers[-1]
        result.append(int(str(first) + str(last)))
    file.close()
    print(sum(result))


part_one()
part_two()
