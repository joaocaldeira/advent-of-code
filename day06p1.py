import csv

with open('input6.txt') as file:
    orbits = list(csv.reader(file))

orbit_dict = {}
for orbit in orbits:
    orbited, orbitee = orbit[0].split(')')
    try:
        orbit_dict[orbited].append(orbitee)
    except KeyError:
        orbit_dict[orbited] = [orbitee]

processing = ['COM']
i = 0
n_orbits = 0
while processing:
    n_orbits += i*len(processing)
    next_to_process = []
    for planet in processing:
        try:
            next_to_process += orbit_dict[planet]
        except KeyError:
            pass
    i += 1
    processing = next_to_process

print(n_orbits)
