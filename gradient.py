from PIL import Image


def gradient(color):
    color = color.lower()
    image = Image.new('RGB', (512, 200), (0, 0, 0))
    pixels = image.load()
    c = 0
    for x in range(0, 512, 2):
        for y in range(200):
            if color == 'r':
                pixels[x, y] = c, 0, 0
                pixels[x + 1, y] = c, 0, 0
            elif color == 'g':
                pixels[x, y] = 0, c, 0
                pixels[x + 1, y] = 0, c, 0
            elif color == 'b':
                pixels[x, y] = 0, 0, c
                pixels[x + 1, y] = 0, 0, c
        c += 1
    image.save('res.png')



