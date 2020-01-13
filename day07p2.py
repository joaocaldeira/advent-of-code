import csv
import itertools


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


def intcode(nums, inputs, ii=0):
    halt = False
    j = 0
    output = []
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
            try:
                nums[nums[ii + 1]] = inputs[j]
            except IndexError:
                return 1, ii, output
            j += 1
            ii += 2
        elif opcode == 4:
            parameters = parse_parameters(1, ii, nums)
            output.append(parameters[0])
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
    return 0, output


with open('input7.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

max_result = 0
for perm in itertools.permutations([5, 6, 7, 8, 9]):
    amp_states = [instructions.copy() for _ in range(5)]
    amp_inputs = [[perm[i]] for i in range(5)]
    amp_inputs[0].append(0)
    amp_cursors = 5*[0]
    i = 0
    while True:
        results = intcode(amp_states[i], amp_inputs[i], amp_cursors[i])
        still_on = results[0]
        if still_on:
            next_curs, next_out = results[1:]
            amp_cursors[i] = next_curs
            amp_inputs[(i+1) % 5] += next_out
            amp_inputs[i] = []
        else:
            if i != 4:
                amp_inputs[(i + 1) % 5] += results[1]
            else:
                output = results[1][-1]
                break
        i = (i+1) % 5

    if output > max_result:
        max_result = output

print(max_result)
