import re

with open('input.txt', 'r') as file:
    data = file.read()
    # Part One
    instructions = []
    for line in data.splitlines():
        instructions.extend(re.findall('mul\(\d+,\d+\)', line))

    result = 0
    for instruction in instructions:
        x, y = map(int, instruction.strip('mul()').split(','))
        result += x * y
    print(result)

    # Part Two
    first_do = data.split("don't()")[0]
    last_do = data.split("do()")[-1]

    dos = [first_do]
    for line in data.splitlines():
        dos.extend(re.findall("do\(\).*?don't\(\)", line))
    dos.append(last_do)

    instructions_dos = []
    for do in dos:
        instructions_dos.extend(re.findall('mul\(\d+,\d+\)', do))

    result_dos = 0
    for instruction_do in instructions_dos:
        x, y = map(int, instruction_do.strip('mul()').split(','))
        result_dos += x * y
    print(result_dos)