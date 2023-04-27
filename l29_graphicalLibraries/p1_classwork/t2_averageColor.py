from PIL import Image


image = Image.open("image.jpg")
width, height = image.size
total_pixels = width * height

r_total, g_total, b_total = 0, 0, 0

for x in range(width):
    for y in range(height):
        r, g, b = image.getpixel((x, y))
        r_total += r
        g_total += g
        b_total += b

r_avg = r_total // total_pixels
g_avg = g_total // total_pixels
b_avg = b_total // total_pixels

print(r_avg, g_avg, b_avg)
