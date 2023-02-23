def create_fractal(num):
    fractal = [0, [1, 1], [1, 1], 2]
    for i in range(num):
        fractal = [0] + fractal + fractal + [2]
