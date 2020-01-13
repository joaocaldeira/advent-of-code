import csv

with open('input6.txt') as file:
    orbits = list(csv.reader(file))

orbit_dict = {}
for orbit in orbits:
    orbited, orbitee = orbit[0].split(')')
    try:
        orbit_dict[orbitee].append(orbited)
    except KeyError:
        orbit_dict[orbitee] = [orbited]

start = orbit_dict['YOU']
end = orbit_dict['SAN']
# there should be a smart way to do this where you don't need to go all the way to COM but can check overlaps as you go
while start[-1] != 'COM':
    start += orbit_dict[start[-1]]
while end[-1] != 'COM':
    end += orbit_dict[end[-1]]

print(2*len(set(start+end)) - len(start) - len(end))
