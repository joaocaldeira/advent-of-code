import csv
import math


class Reaction:
    def __init__(self, reaction_def):
        self.reagents = {}
        for element in reaction_def:
            elements = element.split(' => ')
            if len(elements) == 2:
                simplify = elements[1].strip().split(' ')
                self.product_qty = int(simplify[0])
                self.product = simplify[1]
            simplify = elements[0].strip().split(' ')
            self.reagents[simplify[1]] = int(simplify[0])


with open('input14.txt') as file:
    reaction_list = list(csv.reader(file))

reaction_dict = dict()
for reaction in reaction_list:
    reaction_structured = Reaction(reaction)
    if reaction_structured.product in reaction_dict:
        reaction_dict[reaction_structured.product].append(reaction_structured)
        print('More than one possibility!')
    else:
        reaction_dict[reaction_structured.product] = [reaction_structured]

all_elements = [el for el in reaction_dict] + ['ORE']
elem_index = {el: i for i, el in enumerate(all_elements)}
elements_needed = [[0 for _ in all_elements]]
elements_needed[0][elem_index['FUEL']] = 4052920
j = 0

while j < len(elements_needed):
    while any([needed_num > 0 for needed_num in elements_needed[j][:-1]]):
        for elem in all_elements:
            if elem != 'ORE' and elements_needed[j][elem_index[elem]] > 0:
                for k, reaction in enumerate(reaction_dict[elem]):
                    if k == 0:
                        operating_on = elements_needed[j]
                    else:
                        elements_needed.append(elements_needed[j].copy())
                        operating_on = elements_needed[-1]
                    number_of_reactions = math.ceil(operating_on[elem_index[elem]]/reaction.product_qty)
                    for i, reagent in enumerate(reaction.reagents):
                        operating_on[elem_index[reagent]] += number_of_reactions*reaction.reagents[reagent]
                    operating_on[elem_index[elem]] -= number_of_reactions*reaction.product_qty
    j += 1

print(elements_needed[0][-1])

