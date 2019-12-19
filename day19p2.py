from intcode import Intcode
import csv
import queue

with open('input19.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

i = 0
size = 100
start_j = 0
done = False
right_end = queue.Queue(size)
while not done:
    j = start_j
    found_left = False
    found_right = False
    while not found_right:
        drone = Intcode(instructions)
        results = drone.run([i, j])
        on_beam = results[1][-1]
        if on_beam and not found_left:
            found_left = True
            start_j = j
            j += size - 1
            continue
        elif not on_beam and found_left:
            found_right = True
            right_end.put(j-1)
            if right_end.full():
                top_right_end = right_end.get()
                if top_right_end - start_j >= size - 1:
                    print(10000*(i-size+1)+start_j)
                    done = True
        elif not on_beam and not found_left and j - start_j > 10:
            break
        j += 1
    i += 1
