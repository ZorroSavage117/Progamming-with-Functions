import math

def main():
    radius_list = ['6.83', '7.78', '8.73', '10.32', '10.79', '13.02', '5.40', '6.83', '15.72', '6.83', '7.62', '8.10']
    height_list = ['10.16', '11.91', '11.59', '11.91', '17.78', '14.29', '8.89', '7.62', '17.78', '12.38', '11.27', '11.11']

    i = 0
    while i < len(radius_list):
        radius = float(radius_list[i])
        height = float(height_list[i])
        volume = compute_volume(radius, height)
        surface = compute_surface_area(radius, height)
        storage = compute_storage_efficiency(volume, surface)
        print(f"{i + 1}. volume: {volume:.2f}; surface: {surface:.2f}; storage: {storage:.2f}")
        i += 1

def compute_volume(radius, height):
    vol = math.pi * (radius ** 2) * height
    return vol

def compute_surface_area(radius, height):
    sur_area = (2 * math.pi * radius) * (radius + height) 
    return sur_area

def compute_storage_efficiency(volume, surface_area):
    stor_effcy = volume / surface_area
    return stor_effcy

main()