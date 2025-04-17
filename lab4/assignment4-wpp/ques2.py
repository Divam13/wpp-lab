import math

def count_square_integers(A, B):
    lower = math.ceil(math.sqrt(A))  # Smallest integer whose square is ≥ A
    upper = math.floor(math.sqrt(B))  # Largest integer whose square is ≤ B
    return upper-lower+1 # Count of square numbers

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    A, B = map(int, input().split())
    print(count_square_integers(A, B))
