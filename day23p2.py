from intcode import Intcode
import csv

with open('input23.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

n = 50
computers = [Intcode(instructions, [i]) for i in range(n)]
next_inputs = [[-1] for _ in range(n)]
done = False
previous_delivery = None
nat = None

while not done:
    idle = True
    for i in range(n):
        results = computers[i].run(next_inputs[i])[1]
        next_inputs[i] = [-1]
        for j, address in enumerate(results[::3]):
            idle = False
            if address == 255:
                nat = [results[3*j + 1], results[3*j + 2]]
            elif next_inputs[address][0] == -1:
                next_inputs[address] = [results[3*j + 1], results[3*j + 2]]
            else:
                next_inputs[address] += [results[3*j + 1], results[3*j + 2]]
    if idle:
        if nat is None:
            raise Exception('Machine is idle but no NAT has been given.')
        next_inputs[0] = nat
        if nat == previous_delivery:
            print(nat[1])
            done = True
        previous_delivery = nat
