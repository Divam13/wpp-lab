def utopian_tree(n):
    height = 1  
    for i in range(n):
        if i % 2 == 0:  
            height *= 2  
        else:  
            height += 1  
    return height

T = int(input())  
for _ in range(T):
    N = int(input())
    print(utopian_tree(N))
