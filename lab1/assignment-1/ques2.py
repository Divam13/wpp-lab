import random
list = []
for i in range(100):
    num = random.randint(0,1)
    list.append(num)
count = 0
count_list = []
for i in list:
    if i == 1:
        count_list.append(count)
        count = 0
    else:
        count += 1
print(max(count_list))