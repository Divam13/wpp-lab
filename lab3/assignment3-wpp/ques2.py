def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    
    return b == n

T = int(input())  
for _ in range(T):
    N = int(input())
    if is_fibonacci(N):
        print("IsFibo")
    else:
        print("IsNotFibo")
