import csv
import matplotlib.pyplot as plt

with open('input8.txt') as file:
    image = list(csv.reader(file))[0][0]

n = len(image)
width = 25
height = 6
layer_size = width * height
n_layers = n//layer_size

image_decoded = layer_size*[2]
for i in range(n_layers):
    layer = image[i*layer_size:(i+1)*layer_size]
    for j, char in enumerate(layer):
        if image_decoded[j] == 2 and char != '2':
            image_decoded[j] = int(char)

plt.imshow([image_decoded[j*width:(j+1)*width] for j in range(height)])
plt.show()
