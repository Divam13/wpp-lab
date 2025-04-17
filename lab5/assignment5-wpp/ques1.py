def maximizing_xor(L, R):
    xor_value = L ^ R
    max_xor = 1
    while xor_value:
        max_xor <<= 1
        xor_value >>= 1
    return max_xor - 1

L = int(input().strip())
R = int(input().strip())
print(maximizing_xor(L, R))
