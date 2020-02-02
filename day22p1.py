with open('input22.txt', 'r') as file:
    shuffling_instructions = file.read()

shuffling_instructions = shuffling_instructions.split('\n')
deck_size = 10007

# shuffling_instructions = '''deal with increment 7
# deal into new stack
# deal into new stack'''.split('\n')
# deck_size = 10

deck = [i for i in range(deck_size)]

for command in shuffling_instructions:
    if command.startswith('deal into new stack'):
        deck = deck[::-1]
    elif command.startswith('cut'):
        n_cut = int(command.split(' ')[1])
        deck = deck[n_cut:] + deck[:n_cut]
    elif command.startswith('deal with increment'):
        n_increment = int(command.split(' ')[-1])
        new_deck = deck_size*[0]
        for i in range(deck_size):
            new_pos = n_increment*i % deck_size
            new_deck[new_pos] = deck[i]
        deck = new_deck
    # print(command)
    # print(deck)

print(deck.index(2019))
