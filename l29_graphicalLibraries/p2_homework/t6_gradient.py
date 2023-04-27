from PIL import Image, ImageDraw


def gradient(color):
    color = color.upper()
    size_x, size_y = 512, 200
    new_image = Image.new("RGB", (size_x, size_y), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)

    if color == 'R':
        for i in range(0, size_x, 2):
            draw.rectangle([(i, 0), (i + 1, size_y - 1)], fill=(i // 2, 0, 0))
    elif color == 'G':
        for i in range(0, size_x, 2):
            draw.rectangle([(i, 0), (i + 1, size_y - 1)], fill=(0, i // 2, 0))
    elif color == 'B':
        for i in range(0, size_x, 2):
            draw.rectangle([(i, 0), (i + 1, size_y - 1)], fill=(0, 0, i // 2))
    else:
        raise ValueError("Invalid color input. Only 'R', 'G' and 'B' are allowed.")

    new_image.save('res.png', "PNG")
