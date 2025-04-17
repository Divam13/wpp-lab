import numpy as np

def magic_square_n4():
    n = 4
    magic = np.arange(1, n * n + 1).reshape(n, n)
    flip = np.zeros_like(magic, dtype=bool)
    
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or (i % 4 + j % 4 == 3):
                flip[i, j] = True
    
    magic[flip] = n * n + 1 - magic[flip]
    return magic

def magic_square_odd(n):
    magic = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic[i, j] = num
        i_new, j_new = (i - 1) % n, (j + 1) % n
        if magic[i_new, j_new]:
            i += 1
        else:
            i, j = i_new, j_new
            
    return magic

def magic_square_singly_even(n):
    half_n = n // 2
    sub_square_size = half_n * half_n
    half_square = magic_square_odd(half_n)
    magic = np.zeros((n, n), dtype=int)
    
    magic[:half_n, :half_n] = half_square
    magic[half_n:, half_n:] = half_square + sub_square_size * 2
    magic[:half_n, half_n:] = half_square + sub_square_size * 3
    magic[half_n:, :half_n] = half_square + sub_square_size
    
    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(k):
            magic[i, j], magic[i + half_n, j] = magic[i + half_n, j], magic[i, j]
        for j in range(n - k, n):
            magic[i, j], magic[i + half_n, j] = magic[i + half_n, j], magic[i, j]
    
    j = k
    for i in range(half_n):
        magic[i, j], magic[i + half_n, j] = magic[i + half_n, j], magic[i, j]
    
    return magic

def generate_magic_square(n):
    if n == 4:
        return magic_square_n4()
    elif n % 2 == 1:
        return magic_square_odd(n)
    elif n % 4 == 0:
        return magic_square_n4()
    else:
        return magic_square_singly_even(n)

def main():
    try:
        n = int(input("Enter the size of the magic square (n) between 4 and 8: "))
        if n < 4 or n > 8:
            print("Please enter a value between 4 and 8.")
            return
        
        magic_square = generate_magic_square(n)
        print(f"\nMagic Square for n = {n}:\n")
        print(magic_square)
        print(f"\nSum of each row, column, or diagonal: {n * (n**2 + 1) // 2}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
