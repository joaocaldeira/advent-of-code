how_many = 0
for i in range(271973, 785961):
    list_digits = [int(d) for d in str(i)]
    n = len(list_digits)
    if any([list_digits[j] == list_digits[j+1] for j in range(n-1)]):
        if all([list_digits[j] <= list_digits[j+1] for j in range(n-1)]):
            how_many += 1

print(how_many)
