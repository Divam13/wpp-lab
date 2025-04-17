import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

s_upper = s.str.upper()
print("Upper case:\n", s_upper)

s_lower = s.str.lower()
print("\nLower case:\n", s_lower)

s_length = s.str.len()
print("\nLength of strings:\n", s_length)
