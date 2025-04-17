import numpy as np

def format_strings(arr):
    formatted = {
        "center": np.array([s.center(15, '_') for s in arr]),
        "left": np.array([s.ljust(15, '_') for s in arr]),
        "right": np.array([s.rjust(15, '_') for s in arr]),
    }
    return formatted

def main():
    n = int(input("Enter the number of elements in the array: "))
    print("Enter the strings:")
    elements = [input().strip() for _ in range(n)]
    input_array = np.array(elements, dtype=str)
    formatted_strings = format_strings(input_array)
    print("\nCentered Strings:")
    print(formatted_strings["center"])
    print("\nLeft-Justified Strings:")
    print(formatted_strings["left"])
    print("\nRight-Justified Strings:")
    print(formatted_strings["right"])

if __name__ == "__main__":
    main()
