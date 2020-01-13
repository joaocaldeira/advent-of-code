import csv


def position_or_immediate(mode, number, nums):
    if mode:
        return number
    else:
        return nums[number]


def intcode(nums):
    halt = False
    ii = 0
    while not halt:
        list_digits = [int(d) for d in str(nums[ii]).zfill(4)]
        if list_digits[-1] == 1:
            first_arg = position_or_immediate(list_digits[-3], nums[ii+1], nums)
            second_arg = position_or_immediate(list_digits[-4], nums[ii+2], nums)
            nums[nums[ii + 3]] = first_arg + second_arg
            ii += 4
        elif list_digits[-1] == 2:
            first_arg = position_or_immediate(list_digits[-3], nums[ii + 1], nums)
            second_arg = position_or_immediate(list_digits[-4], nums[ii + 2], nums)
            nums[nums[ii + 3]] = first_arg * second_arg
            ii += 4
        elif list_digits[-1] == 3:
            nums[nums[ii + 1]] = 1
            ii += 2
        elif list_digits[-1] == 4:
            first_arg = position_or_immediate(list_digits[-3], nums[ii + 1], nums)
            print(first_arg)
            ii += 2
        elif int(nums[ii]) == 99:
            halt = True
    return nums[0]


with open('input5.txt') as file:
    instructions = list(csv.reader(file))

instructions = [int(inst) for inst in instructions[0]]
intcode(instructions)
