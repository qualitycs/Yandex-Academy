from PIL import Image, ImageDraw


def cultural_enrichment(filename, w, *colors):
    # Create a new white image
    img = Image.new('RGB', (10 * w, 4 * w), color='white')

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Draw the dish using the specified colors
    dish_color, rect_color, round_color, ellip_color = colors

    draw.ellipse([(0, 0), (10 * w, 4 * w)], fill='green')
    draw.ellipse([(0, w), (0.5 * w, 3 * w)], fill=ellip_color)

    # Save the image to the specified file
    img.save(filename)


# Example usage:
cultural_enrichment('strange_dish.png', 50, 'brown', 'green', 'yellow', 'red')
