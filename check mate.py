from PIL import Image 
from PIL import ImageDraw 


def board(num, size): 
    new_image = Image.new("RGB", (num * size, num * size), (45, 68, 35)) 
    draw = ImageDraw.Draw(new_image) 
    n1 = 0 
    n2 = 0 
    n4 = 0 
    for i in range(num): 
        for i in range(num): 
            if n1 == 0: 
                n3 = n2 + size 
                n5 = n4 + size 
                draw.rectangle((n2, n4, n3, n5), fill=(0, 0, 0), width=0) 
                n2 = n3 
                n1 = 1 
                continue 
            else: 
                n3 = n2 + size 
                n5 = n4 + size 
                draw.rectangle((n2, n4, n3, n5), fill=(255, 255, 255), width=0) 
                n2 = n3 
                n1 = 0 
                continue 
        n4 += size 
        n2, n3, n5 = 0, 0, 0 
        if num % 2 == 0: 
            if n1 == 0: 
                n1 = 1 
            else:
                n1 = 0 
            
    new_image.save('res.png', "PNG")