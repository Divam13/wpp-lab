import pandas as pd
import numpy as np
from itertools import product
concerts = pd.DataFrame({
    'date': pd.to_datetime([
        '2024-01-15', '2024-01-20', '2024-02-10',
        '2024-01-15', '2024-03-05', '2024-02-10'
    ]),
    'artist': ['A', 'B', 'A', 'A', 'C', 'B'],
    'venue': ['X', 'Y', 'Y', 'X', 'Z', 'Y']
})


artists = pd.Series(['A', 'B', 'C'])
venues = pd.Series(['X', 'Y', 'Z'])


artist_venue_pairs = pd.MultiIndex.from_tuples(
    list(product(artists, venues)), names=['artist', 'venue']
)

concerts['year_month'] = concerts['date'].dt.to_period('M')

grouped = concerts.groupby(['year_month', 'artist', 'venue']).size()

year_months = pd.Series(concerts['year_month'].unique())
full_index = pd.MultiIndex.from_product(
    [year_months, artist_venue_pairs],
    names=['year_month', 'artist', 'venue']
)

grouped_full = grouped.reindex(full_index, fill_value=0)

result = grouped_full.unstack(['artist', 'venue']).fillna(0)

result.index = result.index.astype(str)

print(result)
