how_many = 0
for i in range(271973, 785961):
    adjacent = False
    list_digits = [int(d) for d in str(i)]
    if list_digits[0] == list_digits[1]:
        if list_digits[1] != list_digits[2]:
            adjacent = True
    if list_digits[1] == list_digits[2]:
        if list_digits[2] != list_digits[3] and list_digits[0] != list_digits[1]:
            adjacent = True
    if list_digits[2] == list_digits[3]:
        if list_digits[3] != list_digits[4] and list_digits[1] != list_digits[2]:
            adjacent = True
    if list_digits[3] == list_digits[4]:
        if list_digits[4] != list_digits[5] and list_digits[2] != list_digits[3]:
            adjacent = True
    if list_digits[4] == list_digits[5]:
        if list_digits[3] != list_digits[4]:
            adjacent = True

    if adjacent:
        if (list_digits[0] <= list_digits[1] and list_digits[1] <= list_digits[2] and list_digits[2] <= list_digits[3] and
            list_digits[3] <= list_digits[4] and list_digits[4] <= list_digits[5]):
            how_many += 1

print(how_many)