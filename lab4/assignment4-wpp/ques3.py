def is_pangram(s):
    s = s.lower()
    letters = set(s)  
    return all(chr(c) in letters for c in range(ord('a'), ord('z') + 1))

# Read input
s = input("Enter the sentence: ")

# Check if it's a pangram
if is_pangram(s):
    print("pangram")
else:
    print("not pangram")
