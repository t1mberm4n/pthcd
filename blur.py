from PIL import Image, ImageFilter


def motion_blur(n):
    im = Image.open("image.jpg")
    im = im.transpose(Image.ROTATE_270)
    im = im.filter(ImageFilter.GaussianBlur(radius=n))
    im.save("res.jpg")
    return im