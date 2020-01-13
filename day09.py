import csv


def position_or_immediate(mode, number, nums, relative_base):
    try:
        if mode == 1:
            return number
        elif mode == 0:
            return nums[number]
        elif mode == 2:
            return nums[number + relative_base]
    except KeyError:
        return 0


def parse_parameters(how_many, ii, nums, relative_base):
    parameters = []
    list_digits = [int(d) for d in str(nums[ii]).zfill(how_many+2)]
    for i in range(how_many):
        parameters.append(position_or_immediate(list_digits[-3-i], nums[ii+1+i], nums, relative_base))
    return parameters


def intcode(nums, inputs, ii=0):
    halt = False
    j = 0
    output = []
    relative_base = 0
    nums = {jj: inst for jj, inst in enumerate(nums)}
    while not halt:
        opcode = nums[ii] % 100
        if opcode == 1:
            parameters = parse_parameters(2, ii, nums, relative_base)
            list_digits = [int(d) for d in str(nums[ii]).zfill(5)]
            mode = list_digits[0]
            if mode == 0:
                nums[nums[ii + 3]] = parameters[0] + parameters[1]
            elif mode == 2:
                nums[nums[ii + 3] + relative_base] = parameters[0] + parameters[1]
            ii += 4
        elif opcode == 2:
            parameters = parse_parameters(2, ii, nums, relative_base)
            list_digits = [int(d) for d in str(nums[ii]).zfill(5)]
            mode = list_digits[0]
            if mode == 0:
                nums[nums[ii + 3]] = parameters[0] * parameters[1]
            elif mode == 2:
                nums[nums[ii + 3] + relative_base] = parameters[0] * parameters[1]
            ii += 4
        elif opcode == 3:
            list_digits = [int(d) for d in str(nums[ii]).zfill(3)]
            mode = list_digits[0]
            try:
                if mode == 0:
                    nums[nums[ii + 1]] = inputs[j]
                elif mode == 2:
                    nums[nums[ii + 1] + relative_base] = inputs[j]
            except IndexError:
                return 1, ii, output
            j += 1
            ii += 2
        elif opcode == 4:
            parameters = parse_parameters(1, ii, nums, relative_base)
            output.append(parameters[0])
            ii += 2
        elif opcode == 5:
            parameters = parse_parameters(2, ii, nums, relative_base)
            if parameters[0]:
                ii = parameters[1]
                continue
            ii += 3
        elif opcode == 6:
            parameters = parse_parameters(2, ii, nums, relative_base)
            if parameters[0] == 0:
                ii = parameters[1]
                continue
            ii += 3
        elif opcode == 7:
            parameters = parse_parameters(2, ii, nums, relative_base)
            list_digits = [int(d) for d in str(nums[ii]).zfill(5)]
            mode = list_digits[0]
            if mode == 0:
                idx = nums[ii + 3]
            elif mode == 2:
                idx = nums[ii + 3] + relative_base
            if parameters[0] < parameters[1]:
                nums[idx] = 1
            else:
                nums[idx] = 0
            ii += 4
        elif opcode == 8:
            parameters = parse_parameters(2, ii, nums, relative_base)
            list_digits = [int(d) for d in str(nums[ii]).zfill(5)]
            mode = list_digits[0]
            if mode == 0:
                idx = nums[ii + 3]
            elif mode == 2:
                idx = nums[ii + 3] + relative_base
            if parameters[0] == parameters[1]:
                nums[idx] = 1
            else:
                nums[idx] = 0
            ii += 4
        elif opcode == 9:
            parameters = parse_parameters(1, ii, nums, relative_base)
            relative_base += parameters[0]
            ii += 2
        elif opcode == 99:
            halt = True
    return 0, output


with open('input9.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

results = intcode(instructions, [1], 0)

print(results)