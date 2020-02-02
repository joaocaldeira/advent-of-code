def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


with open('input22.txt', 'r') as file:
    shuffling_instructions = file.read()

shuffling_instructions = shuffling_instructions.split('\n')
deck_size = 119315717514047
process_applied = 101741582076661
card_position = 2020

# discover the linear function mapping the final position to the initial one for one shuffle
slope = 1
offset = 0
for command in shuffling_instructions[::-1]:
    if command.startswith('deal into new stack'):
        slope = -slope
        offset = -offset - 1
    elif command.startswith('cut'):
        n_cut = int(command.split(' ')[1])
        offset = offset + n_cut
    elif command.startswith('deal with increment'):
        n_increment = int(command.split(' ')[-1])
        backward_increment = modinv(n_increment, deck_size)
        slope = (slope * backward_increment) % deck_size
        offset = (offset * backward_increment) % deck_size

# map that to the linear function for process_applied shuffles
denominator = modinv(slope - 1, deck_size)
slope_to_n = pow(slope, process_applied, deck_size)
result = (slope_to_n * card_position + offset * denominator * (slope_to_n - 1)) % deck_size

print(result)
