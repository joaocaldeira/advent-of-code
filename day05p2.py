import csv


def position_or_immediate(mode, number, nums):
    if mode:
        return number
    else:
        return nums[number]


def parse_parameters(how_many, ii, nums):
    parameters = []
    list_digits = [int(d) for d in str(nums[ii]).zfill(how_many+2)]
    for i in range(how_many):
        parameters.append(position_or_immediate(list_digits[-3-i], nums[ii+1+i], nums))
    return parameters


def intcode(nums):
    halt = False
    ii = 0
    while not halt:
        opcode = nums[ii] % 100
        if opcode == 1:
            parameters = parse_parameters(2, ii, nums)
            nums[nums[ii + 3]] = parameters[0] + parameters[1]
            ii += 4
        elif opcode == 2:
            parameters = parse_parameters(2, ii, nums)
            nums[nums[ii + 3]] = parameters[0] * parameters[1]
            ii += 4
        elif opcode == 3:
            nums[nums[ii + 1]] = int(input('Give me an integer: '))
            ii += 2
        elif opcode == 4:
            parameters = parse_parameters(1, ii, nums)
            print(parameters[0])
            ii += 2
        elif opcode == 5:
            parameters = parse_parameters(2, ii, nums)
            if parameters[0]:
                ii = parameters[1]
                continue
            ii += 3
        elif opcode == 6:
            parameters = parse_parameters(2, ii, nums)
            if parameters[0] == 0:
                ii = parameters[1]
                continue
            ii += 3
        elif opcode == 7:
            parameters = parse_parameters(2, ii, nums)
            if parameters[0] < parameters[1]:
                nums[nums[ii + 3]] = 1
            else:
                nums[nums[ii + 3]] = 0
            ii += 4
        elif opcode == 8:
            parameters = parse_parameters(2, ii, nums)
            if parameters[0] == parameters[1]:
                nums[nums[ii + 3]] = 1
            else:
                nums[nums[ii + 3]] = 0
            ii += 4
        elif opcode == 99:
            halt = True
    return nums[0]


with open('input5.txt') as file:
    instructions = list(csv.reader(file))

instructions = [int(inst) for inst in instructions[0]]
intcode(instructions)
