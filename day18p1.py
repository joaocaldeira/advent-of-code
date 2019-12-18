def find_distances_to_keys(map_here, starting_pt):
    distances = [float('inf') for _ in map_here]
    distances[starting_pt] = 0
    moves = [1, -1, length, -length]
    current_pos = [starting_pt]
    keys_found = {}
    step = 1

    while current_pos:
        next_pos = []
        for pos in current_pos:
            for move in moves:
                new_pos = pos + move
                if map_here[new_pos] == '.':
                    if step < distances[new_pos]:
                        distances[new_pos] = step
                        next_pos.append(new_pos)
                elif map_here[new_pos].islower() and map_here[new_pos] not in keys_found:
                    keys_found[map_here[new_pos]] = (step, new_pos)
        current_pos = next_pos
        step += 1

    return keys_found


class Path:
    def __init__(self, map_here, steps_so_far, position, keys_found):
        self.map_here = map_here
        self.steps_so_far = steps_so_far
        self.position = position
        self.keys_found = keys_found


with open('input18.txt', 'r') as file:
    underground_map = file.read()

length = underground_map.find('\n') + 1
height = len(underground_map)//length

initial_position = underground_map.find('@')
underground_map = underground_map[:initial_position] + '.' + underground_map[initial_position+1:]

current_maps = [Path(underground_map, 0, initial_position, '')]
min_steps = float('inf')
while current_maps:
    next_maps = {}
    sets_of_keys = {}

    for this_map in current_maps:
        key_distances = find_distances_to_keys(this_map.map_here, this_map.position)

        if not key_distances:
            if min_steps > this_map.steps_so_far:
                min_steps = this_map.steps_so_far
            continue

        for key in key_distances:
            key_pos = this_map.map_here.find(key)
            door_pos = this_map.map_here.find(key.upper())
            new_map = this_map.map_here[:key_pos] + '.' + this_map.map_here[key_pos+1:]
            if door_pos > -1:
                new_map = new_map[:door_pos] + '.' + new_map[door_pos + 1:]

            steps, position = key_distances[key]
            steps_so_far = this_map.steps_so_far + steps

            keys_found = this_map.keys_found + key
            keys_found = ''.join(sorted(keys_found))
            state = (keys_found, position)

            if state not in sets_of_keys or sets_of_keys[state] > steps_so_far:
                sets_of_keys[state] = steps_so_far
                next_maps[state] = Path(new_map, steps_so_far, position, keys_found)

    current_maps = list(next_maps.values())

print(min_steps)
