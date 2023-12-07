from collections import Counter as counter

file = open("daytest.txt", "r")
num_lines = len(file.readlines())
file.seek(0)
values = [0]*num_lines

for lines in range(num_lines):
    line = file.readline()
    line = line.split("\n")[0].split(" ")
    values[lines] = line

dicts = [0]*num_lines
for i in range(num_lines):
    temp_dict = dict(counter(values[i][0]))
    dicts[i] = temp_dict

print(dicts[0])
print(max(dicts[0]))
print(dicts)
print(values)
