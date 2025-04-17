length = int(input('Enter length in feet: '))
length_list = [12 * length, length/3, length/5280, length * 304.8,
length * 30.48, length/3.281, length/3281]
choice = int(input('''1. inches
2. yards
3. miles
4. millimeters
5. centimeters
6. meters
7. kilometers
'''))
print(f'{length_list[choice - 1]:.2f}')