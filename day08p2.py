import csv
import matplotlib.pyplot as plt

with open('input8.txt') as file:
    image = list(csv.reader(file))[0][0]

n = len(image)
layer_size = 25*6
n_layers = n//layer_size

min_digits = 25*6
image_decoded = 150*[2]
for i in range(n_layers):
    layer = image[i*layer_size:(i+1)*layer_size]
    for j, char in enumerate(layer):
        if image_decoded[j] == 2 and char != '2':
            image_decoded[j] = int(char)

plt.imshow([image_decoded[j*25:(j+1)*25] for j in range(6)])
plt.show()
