from PIL import Image


def mirror():
    img = Image.open('image.jpg')
    rotated_img = img.rotate(90, expand=True)
    mirrored_img = rotated_img.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored_img.save('res.jpg')
