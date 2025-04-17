def max_chocolate_pieces(K):
    return K + 1

# Read number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    K = int(input().strip())
    print(max_chocolate_pieces(K))
