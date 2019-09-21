from PIL import Image, ImageDraw


image = Image.new("RGB", (1000, 500), (0, 0, 0))
draw = ImageDraw.Draw(image)
draw.rectangle([(50, 50), (100, 450)], fill='red', outline='blue')
draw.arc([(100, 50), (200, 200)], 270, 450, fill='blue', width=100)
draw.ellipse([(250, 50), (450, 450)], fill='green', outline='green', width=20)
draw.line([(500, 450), (550, 50)], fill='purple', width=20)
draw.line([(550, 50), (600, 200)], fill='purple', width=20)
draw.line([(600, 200), (650, 50)], fill='purple', width=20)
draw.line([(650, 50), (700, 450)], fill='purple', width=20)
draw.pieslice([(750, -350), (950, 450)], 65, 115, fill='yellow', outline='orange', width=10)
draw.line([(830, 250), (870, 250)], fill='purple', width=20)
del draw
image.save("name.png", "PNG")