import math


def find_farthest_orbit(list_of_orbits):
    areas = [(math.pi * a * b, (a, b)) for a, b in list_of_orbits if a != b]
    farthest_orbit = max(areas, key=lambda x: x[0])[1]
    return farthest_orbit
