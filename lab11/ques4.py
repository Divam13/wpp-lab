import pandas as pd
import numpy as np

# Sample schedule for 10 days
df = pd.DataFrame({
    'John': [True, False, False, True, False, False, True, True, False, False],
    'Judy': [False, False, True, True, True, False, True, False, True, True]
})

party_days = df['John'] & df['Judy']
days_til_party = [None] * len(df)

next_party_index = None
for i in reversed(range(len(df))):
    if party_days[i]:
        next_party_index = i
        days_til_party[i] = 0
    elif next_party_index is not None:
        days_til_party[i] = next_party_index - i
    else:
        days_til_party[i] = np.nan  # No party in the future

df['days_til_party'] = days_til_party

print(df)
