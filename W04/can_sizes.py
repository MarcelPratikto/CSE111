import math

#[name, radius, height, cost]
cans = [
    ["Picnic", 6.83, 10.16, 0.28], 
    ["Tall", 7.78, 11.91, 0.43], 
    ["2", 8.73, 11.91, 0.43], 
    ["2.5", 10.32, 11.91, 0.61], 
    ["3 Cylinder", 10.79, 17.78, 0.86], 
    ["5", 13.02, 14.29, 0.83], 
    ["6Z", 5.40, 8.89, 0.22], 
    ["8Z short", 6.83, 7.62, 0.26], 
    ["10", 15.72, 17.78, 1.53], 
    ["211", 6.83, 12.38, 0.34], 
    ["300", 7.62, 11.27, 0.38], 
    ["303", 8.10, 11.11, 0.42]
]

def main():
    
    for i in range(len(cans)):
        name = cans[i][0]
        radius = cans[i][1]
        height = cans[i][2]
        cost = cans[i][3]
        print(f'{name:<10} storage efficiency: {round(calculate_storage_efficiency(radius, height), 1)}   cost efficiency: {round(cost_efficiency(radius, height, cost), 1)}')
    
def cylinder_volume(radius, height):
    volume = math.pi *(radius**2) * height 
    return volume

def cylinder_surface_area(radius, height):
    surface_area = (2 * math.pi) * radius * (radius + height)
    return surface_area

def calculate_storage_efficiency(radius, height):
    # storage efficiency = volume / surface area
    storage_efficiency = (cylinder_volume(radius, height) / cylinder_surface_area(radius, height))
    return storage_efficiency

def cost_efficiency(radius, height, cost):
    cost_efficiency = cylinder_volume(radius, height) / cost
    return cost_efficiency

main()