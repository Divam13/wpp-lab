class_list = []
number_of_students = 4
for i in range(number_of_students):
    name = input('Enter name: ')
    if len(name) <= 15:
        class_list.append(name[::-1])
    else:
        print('Entered name exceeds 15 character')
for i in class_list:
    print(i)
    
