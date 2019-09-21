from PIL import Image


def make_preview(size, n_colors):
    im = Image.open("image.jpg")
    im2 = im.resize(size, resample=0)
    im2 = im2.quantize(colors=n_colors, method=None, kmeans=0, palette=None)
    return im2.save('res.bmp')
