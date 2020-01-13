from collections import Counter

how_many = 0
for i in range(271973, 785961):
    adjacent = False
    list_digits = [int(d) for d in str(i)]
    n = len(list_digits)
    counts = Counter(list_digits)
    if 2 in counts.values() and all([list_digits[j] <= list_digits[j+1] for j in range(n-1)]):
        how_many += 1
    # since digits are non-decreasing, if there are 2 of one digit, they must be next to each other, and vice-versa.

print(how_many)
