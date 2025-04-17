import pandas as pd

asking_prices = pd.Series([15000, 18000, 22000, 17500, 19500])
fair_prices = pd.Series([16000, 17000, 24000, 18000, 19000])

good_deals = asking_prices < fair_prices

good_deal_indices = good_deals[good_deals].index.tolist()

print("Indices of good deals:", good_deal_indices)
