from PIL import Image

lst = [0, 0, 0]
im = Image.open("image.jpg")
pixels = im.load()
x, y = im.size

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        lst[0] += r
        lst[1] += g
        lst[2] += b
print(lst[0] // (x * y), lst[1] // (x * y), lst[2] // (x * y))
