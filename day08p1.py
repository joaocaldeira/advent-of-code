import csv

with open('input8.txt') as file:
    image = list(csv.reader(file))[0][0]

n = len(image)
layer_size = 25*6
n_layers = n//layer_size

min_digits = 25*6
for i in range(n_layers):
    layer = image[i*layer_size:(i+1)*layer_size]
    zero_count = layer.count('0')
    if zero_count < min_digits:
        min_digits = zero_count
        one_count = layer.count('1')
        two_count = layer.count('2')

print(one_count*two_count)
