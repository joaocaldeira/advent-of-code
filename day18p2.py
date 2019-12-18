def find_distances_to_keys(map_here, starting_pts):
    distances = [float('inf') for _ in map_here]
    for pt in starting_pts:
        distances[pt] = 0
    current_pos = [(i, pt) for i, pt in enumerate(starting_pts)]
    moves = [1, -1, length, -length]
    keys_found = {}
    step = 1
    while current_pos:
        next_pos = []
        for pos in current_pos:
            for move in moves:
                new_pos = pos[1] + move
                if map_here[new_pos] == '.':
                    if step < distances[new_pos]:
                        distances[new_pos] = step
                        next_pos.append((pos[0], new_pos))
                elif map_here[new_pos].islower():
                    positions_after_keys = starting_pts.copy()
                    positions_after_keys[pos[0]] = new_pos
                    keys_found[map_here[new_pos]] = (step, positions_after_keys)
        current_pos = next_pos
        step += 1

    return keys_found


class Path:
    def __init__(self, map_here, steps_so_far, positions, keys_found):
        self.map_here = map_here
        self.steps_so_far = steps_so_far
        self.positions = positions
        self.keys_found = keys_found


with open('input18.txt', 'r') as file:
    underground_map = file.read()

# underground_map = '''#######
# #a.#Cd#
# ##...##
# ##.@.##
# ##...##
# #cB#Ab#
# #######
# '''

# underground_map = '''###############
# #d.ABC.#.....a#
# ######...######
# ######.@.######
# ######...######
# #b.....#.....c#
# ###############
# '''

length = underground_map.find('\n') + 1
height = len(underground_map)//length

initial_position = underground_map.find('@')
underground_map = underground_map[:initial_position-1] + '###' + underground_map[initial_position+2:]
underground_map = underground_map[:initial_position-length-1] + '.#.' + underground_map[initial_position-length+2:]
underground_map = underground_map[:initial_position+length-1] + '.#.' + underground_map[initial_position+length+2:]
initial_positions = [initial_position - length - 1, initial_position - length + 1,
                     initial_position + length - 1, initial_position + length + 1]

current_maps = [Path(underground_map, 0, initial_positions, '')]
min_steps = float('inf')
while current_maps:
    next_maps = {}
    sets_of_keys = {}
    for this_map in current_maps:
        key_distances = find_distances_to_keys(this_map.map_here, this_map.positions)
        if not key_distances:
            if min_steps > this_map.steps_so_far:
                min_steps = this_map.steps_so_far
            continue
        for key in key_distances:
            steps, positions = key_distances[key]
            key_pos = this_map.map_here.find(key)
            door_pos = this_map.map_here.find(key.upper())
            new_map = this_map.map_here[:key_pos] + '.' + this_map.map_here[key_pos+1:]
            keys_found = this_map.keys_found + key
            keys_found = ''.join(sorted(keys_found))
            if door_pos > -1:
                new_map = new_map[:door_pos] + '.' + new_map[door_pos + 1:]
            steps_so_far = this_map.steps_so_far + steps
            state = (keys_found, positions[0], positions[1], positions[2], positions[3])
            if state not in sets_of_keys or sets_of_keys[state] > steps_so_far:
                sets_of_keys[state] = steps_so_far
                next_maps[state] = Path(new_map, steps_so_far, positions, keys_found)
    current_maps = list(next_maps.values())

print(min_steps)
