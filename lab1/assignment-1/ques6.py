points= []
print('Enter the points:')
for i in range(5):
    print('Enter point', i+1)
    x = int(input('Enter x coordinate: '))
    y = int(input('Enter y coordinate: '))
    z = int(input('Enter z coordinate: '))
    point = [x, y, z]
    points.append(point)
nearest_neighbour_list = []
for i in points:
    min_distance = float('inf')
    distance = 0
    nearest_point = []
    point_and_neighbour = [i]
    for j in points:
        if i == j:
            continue
        distance = ((i[0] - j[0])**2 + (i[1] - j[1])**2 + (i[2] -
j[2])**2)**0.5
        if distance <= min_distance:
            min_distance = distance
    for j in points:
        if i == j:
            continue
        distance = ((i[0] - j[0])**2 + (i[1] - j[1])**2 + (i[2] -
j[2])**2)**0.5
        if distance == min_distance:
            point_and_neighbour.append(j)
    nearest_neighbour_list.append(point_and_neighbour)
for i in nearest_neighbour_list:
    print(f'[Point, Nearest Neighbours]={i}')