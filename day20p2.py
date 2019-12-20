from collections import defaultdict

with open('input20.txt', 'r') as file:
    maze_map = file.read()

# maze_map = ('         A           \n'
#             '         A           \n'
#             '  #######.#########  \n'
#             '  #######.........#  \n'
#             '  #######.#######.#  \n'
#             '  #######.#######.#  \n'
#             '  #######.#######.#  \n'
#             '  #####  B    ###.#  \n'
#             'BC...##  C    ###.#  \n'
#             '  ##.##       ###.#  \n'
#             '  ##...DE  F  ###.#  \n'
#             '  #####    G  ###.#  \n'
#             '  #########.#####.#  \n'
#             'DE..#######...###.#  \n'
#             '  #.#########.###.#  \n'
#             'FG..#########.....#  \n'
#             '  ###########.#####  \n'
#             '             Z       \n'
#             '             Z       \n')

width = maze_map.find('\n') + 1
maze_size = len(maze_map)

portal_starts = {}
portal_maps_up = {}
portal_maps_down = {}

for i, char in enumerate(maze_map):
    if char.isupper():
        if maze_map[i+1].isupper():
            key = maze_map[i:i+2]
            if maze_map[i+2] == '.':
                address = i + 2
            else:
                address = i - 1
            going_up = (maze_map[i+2] == '\n') or (maze_map[i-1] == '\n')
        elif i+width < maze_size and maze_map[i + width].isupper():
            key = char + maze_map[i + width]
            if i+2*width < maze_size and maze_map[i + 2 * width] == '.':
                address = i + 2 * width
            else:
                address = i - width
            going_up = (i + 2 * width > maze_size) or (i - width < 0)
        if key:
            if key in portal_starts:
                if going_up:
                    portal_maps_up[address] = portal_starts[key]
                    portal_maps_down[portal_starts[key]] = address
                else:
                    portal_maps_down[address] = portal_starts[key]
                    portal_maps_up[portal_starts[key]] = address
            else:
                portal_starts[key] = address
        key = None

starting_pt = portal_starts['AA']
goal = portal_starts['ZZ']

distances = defaultdict(lambda: float('inf'), {})
distances[(0, starting_pt)] = 0
moves = [1, -1, width, -width]
current_pos = [(0, starting_pt)]
step = 1
done = False

while not done:
    next_pos = []
    for pos in current_pos:
        new_pos_list = [(pos[0], pos[1] + move) for move in moves]
        if pos[1] in portal_maps_up and pos[0] > 0:
            new_pos_list.append((pos[0]-1, portal_maps_up[pos[1]]))
        if pos[1] in portal_maps_down:
            new_pos_list.append((pos[0]+1, portal_maps_down[pos[1]]))
        for new_pos in new_pos_list:
            if new_pos == (0, goal):
                print(step)
                done = True
            if maze_map[new_pos[1]] == '.':
                if step < distances[new_pos]:
                    distances[new_pos] = step
                    next_pos.append(new_pos)
    current_pos = next_pos
    step += 1
