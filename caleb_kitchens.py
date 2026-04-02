def rect_surface_are(length, width, height):
    total = rect_area(length, height) * 4
    total += rect_area(height, width) * 2
    return total