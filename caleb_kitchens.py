#caleb_kitchens.py
#Written by Caleb Kitchens
#Function: rect_surface_area
def rect_surface_area(length, width, height):
    total = rect_area(length, height) * 4
    total += rect_area(height, width) * 2
    return total