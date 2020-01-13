from collections import defaultdict


parameters_per_opcode = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]


class Parameter:
    def __init__(self, mode, machine, input_instr):
        if mode == 0:
            self.address = input_instr
            self.value = machine.instructions[self.address]
        elif mode == 1:
            self.address = None
            self.value = input_instr
        elif mode == 2:
            self.address = input_instr + machine.relative_base
            self.value = machine.instructions[self.address]


class Intcode:
    def __init__(self, instructions, inputs=None):
        self.instructions = defaultdict(lambda: 0, {jj: inst for jj, inst in enumerate(instructions)})
        if inputs is None:
            self.inputs = []
        else:
            self.inputs = inputs
        self.cursor = 0
        self.relative_base = 0
        self.halted = False

    def parse_parameters(self, how_many):
        parameters = []
        list_digits = [int(d) for d in str(self.instructions[self.cursor]).zfill(how_many+2)]
        for i in range(how_many):
            parameters.append(Parameter(list_digits[-3-i], self, self.instructions[self.cursor+1+i]))
        return parameters

    def run(self, inputs=None):
        j = 0
        if inputs is not None:
            self.inputs = self.inputs + inputs
        output = []
        while not self.halted:
            opcode = self.instructions[self.cursor] % 100
            if opcode < 99:
                parameters = self.parse_parameters(parameters_per_opcode[opcode])

                if opcode == 1:
                    self.instructions[parameters[2].address] = parameters[0].value + parameters[1].value
                elif opcode == 2:
                    self.instructions[parameters[2].address] = parameters[0].value * parameters[1].value
                elif opcode == 3:
                    try:
                        self.instructions[parameters[0].address] = self.inputs[j]
                        j += 1
                    except IndexError:
                        self.inputs = []
                        return 1, output
                elif opcode == 4:
                    output.append(parameters[0].value)
                elif opcode == 5:
                    if parameters[0].value:
                        self.cursor = parameters[1].value
                        continue
                elif opcode == 6:
                    if parameters[0].value == 0:
                        self.cursor = parameters[1].value
                        continue
                elif opcode == 7:
                    if parameters[0].value < parameters[1].value:
                        self.instructions[parameters[2].address] = 1
                    else:
                        self.instructions[parameters[2].address] = 0
                elif opcode == 8:
                    if parameters[0].value == parameters[1].value:
                        self.instructions[parameters[2].address] = 1
                    else:
                        self.instructions[parameters[2].address] = 0
                elif opcode == 9:
                    self.relative_base += parameters[0].value

                self.cursor += parameters_per_opcode[opcode] + 1
            else:
                self.halted = True
        return 0, output
